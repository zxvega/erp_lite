from django.contrib import admin
from .models import *

# Register your models here.

# Contact

class ContactAdmin(admin.ModelAdmin):
    exclude = ['created_by','modified_by']
    search_fields = ['name','last_name']
    list_display = ('id','name','last_name','document','addres','telephone','email')
    readonly_fields = ('created','modified','created_by','modified_by',)
    fieldsets = [
        ( None, {'fields':['name','last_name','document','addres','telephone','email']}),
        ( 'Registro de auditoria', {'fields': ['created','modified','created_by','modified_by',]})
    ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
            obj.modified_by = request.user
        else:
            obj.modified_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Contact, ContactAdmin)