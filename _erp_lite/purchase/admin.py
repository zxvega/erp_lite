from rangefilter.filters import DateRangeFilterBuilder
from django.utils.html import mark_safe
from django.contrib import admin
from django.urls import reverse
from .models import *
from core.mixins import *

# Register your models here.

class PurchaseDetailInline(admin.TabularInline):
    model = PurchaseDetail
    autocomplete_fields = ('product',)
    extra = 0
    min_num = 1

class PurchaseAdmin(WeasyPrintMixin,admin.ModelAdmin):
    list_display = ('id', 'date','supplier','get_total','print')
    inlines = [PurchaseDetailInline]
    autocomplete_fields = ('supplier',)
    exclude = ['created_by','modified_by']
    list_filter = (('date',DateRangeFilterBuilder()),)
    print_template = 'print/purchase.html'

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    # Enlaces a las vistas

    def get_total(self, obj):
        sale = Purchase.objects.get(pk=obj.id)
        return sum(detail.subtotal for detail in sale.details.all())
    
    get_total.short_description = 'Total Compra'
    
    def print(self, obj):
        url_name = f'admin:{obj._meta.app_label}_{obj._meta.model_name}_print'
        url = reverse(url_name, args=[obj.id])
        link = f'<a href="{url}" target="_blank"><b>Imprimir</b></a>'
        return mark_safe(link)
    
    print.short_description = 'Nota de Compra'

    # Vistas sobrescritas

    def print_view(self, request, model_id):
        sale = Purchase.objects.get(pk=model_id)
        self.print_data['subtotal_sum'] = sum(detail.subtotal for detail in sale.details.all())
        return super().print_view(request, model_id)

admin.site.register(Purchase, PurchaseAdmin)