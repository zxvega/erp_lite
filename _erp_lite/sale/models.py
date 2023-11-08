from django.db import models
from core.utils import get_price
from core.models import CoreModel
from product.models import Product
from django.contrib.auth.models import User, Group
from contact.models import Contact

# Create your models here.

class Sale(CoreModel):
    date = models.DateField(verbose_name='Fecha')
    customer = models.ForeignKey(Contact, null=True, blank=True, related_name = 'customer_sales', on_delete=models.PROTECT,verbose_name='Cliente') 
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return 'Venta: ' + str(self.id)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        permissions = [
            ("export_sale","Can export sale"),
        ]

class SaleDetail(CoreModel):
    sale = models.ForeignKey(Sale, related_name='details',blank=True, null=True ,on_delete=models.CASCADE,verbose_name='Detalle')
    product = models.ForeignKey(Product, related_name='sales',blank=True, null=True, on_delete=models.PROTECT,verbose_name='Producto')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=get_price())
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return 'Detalle: ' + str(self.id)

    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalle'