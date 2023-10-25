from django.db import models
from core.models import CoreModel
from product.models import Product
from django.contrib.auth.models import User, Group

# Create your models here.

class Location(CoreModel):
    name = models.CharField(max_length=255, default='', verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created_by = models.ForeignKey(User, null=True, blank=True, related_name = 'created_locations', on_delete=models.PROTECT, verbose_name='Creado por')
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name = 'modified_locations', on_delete=models.PROTECT, verbose_name='Modificado por')
    
    class Meta:
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'
        permissions = [
            ("export_location","Can export location"),
            ("import_location","Can import location")
        ]
    
    def __str__(self):
        return self.name
    

    