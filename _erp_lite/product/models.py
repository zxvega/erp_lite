from django.db import models
from core.models import CoreModel
from django.contrib.auth.models import User, Group

# Create your models here.

class Category(CoreModel):
    name = models.CharField(max_length=255, default='', verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created_by = models.ForeignKey(User, null=True, blank=True, related_name = 'created_categories', on_delete=models.PROTECT, verbose_name='Creado por')
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name = 'modified_categories', on_delete=models.PROTECT, verbose_name='Modificado por')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        permissions = [
            ("export_category","Can export category"),
            ("import_category","Can import category")
        ]
    
    def __str__(self):
        return self.name


class Product(CoreModel):
    name = models.CharField(max_length=255, default='', verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    category = models.ForeignKey(Category, null=True, blank=True, related_name = 'products', on_delete=models.PROTECT, verbose_name='Categoria')
    created_by = models.ForeignKey(User, null=True, blank=True, related_name = 'created_products', on_delete=models.PROTECT, verbose_name='Creado por')
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name = 'modified_products', on_delete=models.PROTECT, verbose_name='Modificado por')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        permissions = [
            ("export_product","Can export product"),
            ("import_product","Can import product")
        ]
    
    def __str__(self):
        return self.name