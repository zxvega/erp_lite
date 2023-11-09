from import_export.admin import ExportActionMixin
from django.contrib.admin.models import LogEntry
from django.contrib import admin
from .models import * 

# Register your models here.

class LogAdmin(ExportActionMixin,admin.ModelAdmin):
    search_fields = ['user__username']
    search_help_text = "Busqueda por Usuario"
    list_display = ('id','content_type','object_repr','action_flag','user','action_time')
    list_filter = ('action_flag','content_type')
    list_per_page = 10

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(LogEntry,LogAdmin)

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