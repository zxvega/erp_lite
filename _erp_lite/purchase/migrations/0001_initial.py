# Generated by Django 4.2.3 on 2023-10-23 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0004_alter_category_active_alter_product_active'),
        ('contact', '0003_contact_email_alter_contact_addres_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Fecha modificacion')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_purchases', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modified_purchases', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='supplier_purchase', to='contact.contact', verbose_name='Proveedor')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'permissions': [('export_purchase', 'Can export purchase')],
            },
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Fecha modificacion')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('quantity', models.IntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=12)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='purchases', to='product.product', verbose_name='Producto')),
                ('purchase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='purchase.purchase', verbose_name='Detalle')),
            ],
            options={
                'verbose_name': 'Detalle',
                'verbose_name_plural': 'Detalle',
            },
        ),
    ]
