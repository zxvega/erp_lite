from django.conf import settings
from django.db import models

# Create your models here.

class CoreModel(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha modificacion')

    class Meta:
        abstract = True

    
class EmailLog(CoreModel):
    to =  models.EmailField(max_length=254, null = True, blank = True)
    subject = models.CharField(max_length=254, verbose_name='Destinatario')
    content = models.TextField(verbose_name='Contenido')
    response = models.TextField(verbose_name='Respuesta')

    class Meta:
        verbose_name = 'Registro de email'
        verbose_name_plural = 'Registro de emails'
    
    def __str__(self):
        return 'Email: #'  + str(self.id)