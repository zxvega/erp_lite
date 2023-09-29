from django.contrib import admin
from .models import * 

# Register your models here.

# Registro de email

class EmailLogAdmin(admin.ModelAdmin):
    pass

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(EmailLog, EmailLogAdmin)