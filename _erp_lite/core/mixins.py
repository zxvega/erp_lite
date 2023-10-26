from django.urls import path
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from wkhtmltopdf.views import PDFTemplateResponse
from .utils import create_mail
from .models import EmailLog
from django.contrib import messages
import threading
from weasyprint import HTML, CSS
from django_weasyprint import WeasyTemplateResponseMixin
from django.template.loader import get_template
from django.http import HttpResponse

class ReportMixin:

    print_template = ''
    print_data = {}

    def get_urls(self):
        urls = super().get_urls()
        app_label = self.model._meta.app_label
        custom_urls = [
            path(
                '<int:model_id>/print/', 
                 self.admin_site.admin_view(self.print_view), 
                 name=f'{app_label}_{self.model._meta.model_name}_print'
                 ),
        ]
        return custom_urls + urls
    
    def print_view(self, request, model_id):
        obj = get_object_or_404(self.model, pk=model_id)
        name = f'{self.model._meta.model_name}_print_{model_id}_pdf'
        self.print_data['debug']: settings.DEBUG
        self.print_data['obj']= obj
        response = PDFTemplateResponse(
            request=request,
            template=self.print_template,
            filename= name,
            context = self.print_data,
            show_content_in_browser=True,
            cmd_options={
                'margin-top': 10, 
                "zoom":1, 
                "viewport-size" :"1366 x 513", 
                'javascript-delay':1000, 
                'footer-right' :'[page]/[topage]', 
                'footer-font-size' : 8 ,
                "no-stop-slow-scripts":True,
                
                }
        )
        return response
    

class EmailMixin:

    email_template = ''
    email_data = {}
    subject = ''
    to = None

    def get_urls(self):
        urls = super().get_urls()
        app_label = self.model._meta.app_label
        custom_urls = [
            path(
                '<int:model_id>/email/', 
                 self.admin_site.admin_view(self.email_view), 
                 name=f'{app_label}_{self.model._meta.model_name}_email'
                 ),
        ]
        return custom_urls + urls
    
    def send_email_thread(self, email):
        email.send(fail_silently=False)
    
    def email_view(self, request, model_id):
        obj = get_object_or_404(self.model, pk=model_id)
        self.email_data['obj']= obj
        email = create_mail(
            self.to,
            self.subject,
            self.email_template,
            self.email_data
        ) 
        response = ''
        try:
            email_thread = threading.Thread(target=self.send_email_thread, args=(email,))
            email_thread.start()
        except Exception as e:
            response = str(e)
        else:
            response = "Mensaje Enviado"
        finally:
            email_log = EmailLog(to = self.to,subject = self.subject,content= email.alternatives[0][0], response= response)
            email_log.save()

        messages.success(request, 'El correo electrónico se está enviando en segundo plano, puedes revisar el registro de emails')

        return redirect(request.META.get('HTTP_REFERER'))


class ReportEmailMixin(ReportMixin, EmailMixin):
    pass


class WeasyPrintMixin:

    print_template = ''
    print_data = {}

    def get_urls(self):
        urls = super().get_urls()
        app_label = self.model._meta.app_label
        custom_urls = [
            path(
                '<int:model_id>/print/', 
                 self.admin_site.admin_view(self.print_view), 
                 name=f'{app_label}_{self.model._meta.model_name}_print'
                 ),
        ]
        return custom_urls + urls
    
    def print_view(self, request, model_id):
        obj = get_object_or_404(self.model, pk=model_id)
        name = f'{self.model._meta.model_name}_print_{model_id}_pdf'
        self.print_data['obj']= obj

        # Renderizar el template con el contexto
        context = self.print_data  # Puedes agregar más contexto si es necesario
        html_template = get_template(self.print_template)
        html_string = html_template.render(context)

        # Crear un objeto WeasyPrint HTML desde la cadena HTML
        html = HTML(string=html_string, base_url=request.build_absolute_uri())

        # Generar el PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{name}.pdf"'
        html.write_pdf(response)

        return response