from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

def get_price():
    return 25

def create_mail(email, subject, template_name, context):
    template = get_template(template_name)
    content = template.render(context)

    message = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=settings.EMAIL_HOST_USER,
        to=[
            email
        ],
        cc=[]
    )

    message.attach_alternative(content, 'text/html')
    return message