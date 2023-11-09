
from import_export.admin import ImportExportMixin
from django.contrib import admin
from .models import *
from .filters import CategoryFilter
from .forms import ProductModelForm

# Register your models here.

# Categoria

class CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name','active')
    readonly_fields = ('created','modified','created_by','modified_by',)
    exclude = ['created_by','modified_by']
    fieldsets = [
        ( None, {'fields':['name','active']}),
        ( 'Registro de auditoria', {'fields': ['created','modified','created_by','modified_by',]})
    ]
    ordering = ('name',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
            obj.modified_by = request.user
        else:
            obj.modified_by = request.user
        super().save_model(request, obj, form, change)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            queryset = queryset.filter(active=True)
        return queryset, use_distinct


admin.site.register(Category, CategoryAdmin)

# Producto

class ProductAdmin(ImportExportMixin,admin.ModelAdmin):
    form = ProductModelForm
    search_fields = ['name']
    exclude = ['created_by','modified_by']
    list_display = ('id', 'name','category','can_be_sale','can_be_purchased','active')
    list_filter = (CategoryFilter,)
    readonly_fields = ('created','modified','created_by','modified_by',)
    fieldsets = [
        ( None, {'fields':['name','category','can_be_sale','can_be_purchased','active']}),
        ( 'Registro de auditoria', {'fields': ['created','modified','created_by','modified_by',]})
    ]
    ordering = ('name',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
            obj.modified_by = request.user
        else:
            obj.modified_by = request.user
        super().save_model(request, obj, form, change)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            app_label = request.GET.get('app_label')
            if app_label == 'sale':
                queryset = queryset.filter(active=True, can_be_sale=True)
            if app_label == 'purchase':
                queryset = queryset.filter(active=True, can_be_purchased=True)
            queryset = queryset.filter(active=True)
        return queryset, use_distinct

admin.site.register(Product, ProductAdmin)