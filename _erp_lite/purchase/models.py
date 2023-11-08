from django.db import models
from core.models import CoreModel
from product.models import Product
from django.contrib.auth.models import User, Group
from contact.models import Contact

# Create your models here.

class Purchase(CoreModel):
    date = models.DateField(verbose_name='Fecha')
    supplier = models.ForeignKey(Contact, null=True, blank=True, related_name = 'supplier_purchase', on_delete=models.PROTECT,verbose_name='Proveedor') 
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return 'Compra: ' + str(self.id)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        permissions = [
            ("export_purchase","Can export purchase"),
        ]

class PurchaseDetail(CoreModel):
    purchase = models.ForeignKey(Purchase, related_name='details',blank=True, null=True ,on_delete=models.CASCADE,verbose_name='Detalle')
    product = models.ForeignKey(Product, related_name='purchases',blank=True, null=True, on_delete=models.PROTECT,verbose_name='Producto')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return 'Detalle: ' + str(self.id)

    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalle'