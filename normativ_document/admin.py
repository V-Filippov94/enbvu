from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class ContentNormAktAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Контент')

    class Meta:
        model: ContentNormAkt
        fields: '__all__'


class ListFileNormAktAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Контент')

    class Meta:
        model: ListFileNormAkt
        fields: '__all__'


class ListFileNormAktInline(admin.TabularInline):
    form = ListFileNormAktAdminForm
    model = ListFileNormAkt

    def get_extra(self, request, obj=None, **kwargs):
        return 1 if obj else 3


class FileNormAktInline(admin.TabularInline):
    model = FileNormAkt


class ContentNormAktAdmin(admin.ModelAdmin):
    form = ContentNormAktAdminForm
    inlines = [ListFileNormAktInline, FileNormAktInline]
    list_display = ('title', 'un_menu_norm_akt', 'date_change')
    list_display_links = ('title', 'un_menu_norm_akt')
    list_filter = ('date_change', 'un_menu_norm_akt')
    fields = ('title', 'content', 'mode_page', 'un_menu_norm_akt', 'date_created', 'date_change')
    readonly_fields = ('date_change',)
    search_fields = ('title', 'date_created', 'un_menu_norm_akt', 'date_change', 'content')


admin.site.register(ContentNormAkt, ContentNormAktAdmin)
# admin.site.register(UnMenuNormAkt)