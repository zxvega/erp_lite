from django.contrib import admin
from .models import *

# Register your models here.

# Producto

class LocationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    exclude = ['created_by','modified_by']
    list_display = ('id', 'name','active')
    readonly_fields = ('created','modified','created_by','modified_by',)
    fieldsets = [
        ( None, {'fields':['name','active']}),
        ( 'Registro de auditoria', {'fields': ['created','modified','created_by','modified_by',]})
    ]

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

admin.site.register(Location, LocationAdmin)