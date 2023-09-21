from rangefilter.filters import DateRangeFilterBuilder
from django.utils.html import mark_safe
from django.contrib import admin
from django.urls import reverse
from .models import *
from core.mixins import *

# Register your models here.

# Venta

class SaleDetailInline(admin.TabularInline):
    model = SaleDetail
    autocomplete_fields = ('product',)
    extra = 0
    min_num = 1

class SaleAdmin(ReportMixin,admin.ModelAdmin):
    list_display = ('id', 'date','customer','get_total','print')
    inlines = [SaleDetailInline]
    autocomplete_fields = ('customer',)
    exclude = ['created_by','modified_by']
    list_filter = (('date',DateRangeFilterBuilder()),)
    print_template = 'print/sale.html'

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    def get_total(self, obj):
        sale = Sale.objects.get(pk=obj.id)
        return sum(detail.subtotal for detail in sale.details.all())
    
    get_total.short_description = 'Total Venta'
    
    def print(self, obj):
        url_name = f'admin:{obj._meta.app_label}_{obj._meta.model_name}_print'
        url = reverse(url_name, args=[obj.id])
        link = f'<a href="{url}" target="_blank"><b>Imprimir</b></a>'
        return mark_safe(link)
    
    print.short_description = 'Nota de Venta'

    def print_view(self, request, model_id):
        sale = Sale.objects.get(pk=model_id)
        self.print_data['subtotal_sum'] = sum(detail.subtotal for detail in sale.details.all())
        return super().print_view(request, model_id)
    
admin.site.register(Sale, SaleAdmin)