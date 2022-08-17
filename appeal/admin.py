from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class ContentAppealAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Контент')

    class Meta:
        model: ContentAppeal
        fields: '__all__'


class ListFileAppealAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Контент')

    class Meta:
        model: ListFileAppeal
        fields: '__all__'


class ListFileAppealInline(admin.TabularInline):
    form = ListFileAppealAdminForm
    model = ListFileAppeal

    def get_extra(self, request, obj=None, **kwargs):
        return 1 if obj else 3


class FileAppealInline(admin.TabularInline):
    model = FileAppeal


class ContentAppealAdmin(admin.ModelAdmin):
    form = ContentAppealAdminForm
    inlines = [ListFileAppealInline, FileAppealInline]
    list_display = ('title', 'un_menu_appeal', 'date_change')
    list_display_links = ('title', 'un_menu_appeal')
    list_filter = ('date_change', 'un_menu_appeal')
    fields = ('title', 'content', 'mode_page', 'un_menu_appeal', 'date_created', 'date_change')
    readonly_fields = ('date_change',)
    search_fields = ('title', 'date_created', 'un_menu_appeal', 'date_change', 'content')


class AppealModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'message', 'file', 'date_created')
    list_display_links = ('name', 'email', 'address', 'message')
    search_fields = ('name', 'email', 'address', 'date_created')
    list_filter = ('name', 'email', 'address', 'date_created')


# admin.site.register(UnMenuAppeal)
admin.site.register(AppealModel, AppealModelAdmin)
admin.site.register(ContentAppeal, ContentAppealAdmin)
