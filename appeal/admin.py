from django.contrib import admin
from .models import AppealModel


class AppealModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'message', 'file', 'date_created')
    list_display_links = ('name', 'email', 'address', 'message')
    search_fields = ('name', 'email', 'address', 'date_created')
    list_filter = ('name', 'email', 'address', 'date_created')


admin.site.register(AppealModel, AppealModelAdmin)
