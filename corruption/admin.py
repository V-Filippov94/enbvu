from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class ContentCorruptionAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Контент')

    class Meta:
        model: ContentCorruption
        fields: '__all__'


class ListFileCorruptionAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Контент')

    class Meta:
        model: ListFileCorruption
        fields: '__all__'


class ListFileCorruptionInline(admin.TabularInline):

    form = ListFileCorruptionAdminForm
    model = ListFileCorruption
    # def get_extra(self, request, obj=None, **kwargs):
    #     return 1 if obj else 3


class FileCorruptionInline(admin.TabularInline):
    model = FileCorruption


class ContentCorruptionAdmin(admin.ModelAdmin):
    form = ContentCorruptionAdminForm
    inlines = [ListFileCorruptionInline, FileCorruptionInline]
    list_display = ('title', 'un_menu_corruption', 'date_change')
    list_display_links = ('title', 'un_menu_corruption')
    list_filter = ('date_change', 'un_menu_corruption')
    fields = ('title', 'content', 'mode_page', 'un_menu_corruption', 'date_created', 'date_change')
    readonly_fields = ('date_change',)
    search_fields = ('title', 'date_created', 'un_menu_corruption', 'date_change', 'content')


# admin.site.register(UnMenuCorruption)
admin.site.register(ContentCorruption, ContentCorruptionAdmin)
admin.site.register(AppealAntiCorruption)