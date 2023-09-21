from django.urls import path
from django.conf import settings
from django.shortcuts import get_object_or_404
from wkhtmltopdf.views import PDFTemplateResponse

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

    def get_urls(self):
        urls = super().get_urls()
        app_label = self.model._meta.app_label
        custom_urls = [
            path(
                '<int:model_id>/email/', 
                 self.admin_site.admin_view(self.print_view), 
                 name=f'{app_label}_{self.model._meta.model_name}_email'
                 ),
        ]
        return custom_urls + urls
    
    def email_view(self, request, model_id):
        pass