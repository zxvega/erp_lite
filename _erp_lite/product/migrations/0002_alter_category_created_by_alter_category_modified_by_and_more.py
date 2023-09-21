# Generated by Django 4.2.3 on 2023-09-06 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_categories', to=settings.AUTH_USER_MODEL, verbose_name='Creado por'),
        ),
        migrations.AlterField(
            model_name='category',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modified_categories', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='product.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_products', to=settings.AUTH_USER_MODEL, verbose_name='Creado por'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modified_products', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Nombre'),
        ),
    ]