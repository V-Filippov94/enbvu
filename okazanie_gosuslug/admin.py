from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class ContentOkazanieGosuslugAdminForm(forms.ModelForm):
    content_okazanie_gosuslug = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Контент')

    class Meta:
        model: ContentOkazanieGosuslug
        fields: '__all__'


class ListFileOkazanieGosuslugAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Контент')

    class Meta:
        model: ListFileOkazanieGosuslug
        fields: '__all__'


class ListFileOkazanieGosuslugInline(admin.TabularInline):
    form = ListFileOkazanieGosuslugAdminForm
    model = ListFileOkazanieGosuslug

    def get_extra(self, request, obj=None, **kwargs):
        return 1 if obj else 3


class FileOkazanieGosuslugInline(admin.TabularInline):
    model = FileOkazanieGosuslug


class ContentOkazanieGosuslugAdmin(admin.ModelAdmin):
    form = ContentOkazanieGosuslugAdminForm
    inlines = [ListFileOkazanieGosuslugInline, FileOkazanieGosuslugInline]
    list_display = ('title', 'un_menu_okazanie_gosuslug', 'date_change')
    list_display_links = ('title', 'un_menu_okazanie_gosuslug')
    list_filter = ('date_change', 'un_menu_okazanie_gosuslug')
    fields = (
    'title', 'content_okazanie_gosuslug', 'mode_page', 'un_menu_okazanie_gosuslug', 'date_created', 'date_change')
    readonly_fields = ('date_change',)
    search_fields = ('title', 'date_created', 'un_menu_okazanie_gosuslug', 'date_change', 'content_okazanie_gosuslug')


# admin.site.register(UnMenuOkazanieGosuslug)
admin.site.register(ContentOkazanieGosuslug, ContentOkazanieGosuslugAdmin)
