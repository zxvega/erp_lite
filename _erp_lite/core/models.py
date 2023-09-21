from django.conf import settings
from django.db import models

# Create your models here.

class CoreModel(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha modificacion')

    class Meta:
        abstract = True