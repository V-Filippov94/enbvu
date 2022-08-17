from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class KadrProvisionAdminForm(forms.ModelForm):
    content_kadr = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Текст страницы')

    class Meta:
        model: KadrProvision
        fields: '__all__'


class ListFileKadrAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Текст страницы')

    class Meta:
        model: ListFileKadr
        fields: '__all__'


class ListFileKadrInline(admin.TabularInline):
    form = ListFileKadrAdminForm
    model = ListFileKadr

    def get_extra(self, request, obj=None, **kwargs):
        return 1 if obj else 3


class FileKadrInline(admin.TabularInline):
    model = FileKadr


class KadrProvisionAdmin(admin.ModelAdmin):
    form = KadrProvisionAdminForm
    inlines = [ListFileKadrInline, FileKadrInline]
    list_display = ('title',  'date_change')
    list_display_links = ('title', 'date_change')
    list_filter = ('date_change', 'un_page')
    fields = ('title', 'content_kadr', 'date_created', 'date_change', 'mode_page', 'un_page')
    readonly_fields = ('date_change',)
    search_fields = ('title', 'content_kadr', 'date_created', 'date_change', 'un_page')


# admin.site.register(UnPageKadr)
admin.site.register(KadrProvision, KadrProvisionAdmin)
