from django.db import models
from core.models import CoreModel
from django.contrib.auth.models import User, Group
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Contact(CoreModel):
    name = models.CharField(max_length=254, verbose_name='Nombre')
    last_name = models.CharField(max_length=254, verbose_name='Apellido')
    document = models.IntegerField(verbose_name='Documento de Identidad', blank=True, null=True )
    addres = models.CharField(max_length=254, blank=True, null=True, verbose_name='Dirección')
    telephone = PhoneNumberField(unique = False, null = False, blank = False, verbose_name='Telefono') 
    email = models.EmailField(max_length=254, null = True, blank = True)

    def __str__(self):
        return self.name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'