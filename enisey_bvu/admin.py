from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class ContentAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Контент')

    class Meta:
        model: Content
        fields: '__all__'


class ListFileAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Контент')

    class Meta:
        model: Content
        fields: '__all__'


class ListFileInline(admin.TabularInline):
    form = ListFileAdminForm
    model = ListFile

    def get_extra(self, request, obj=None, **kwargs):
        return 1 if obj else 1


class FileInline(admin.TabularInline):
    model = File


class ContentAdmin(admin.ModelAdmin):
    form = ContentAdminForm
    inlines = [ListFileInline, FileInline]
    list_display = ('title', 'un_menu_enbv',  'date_change')
    list_display_links = ('title', 'un_menu_enbv')
    list_filter = ('date_change', 'un_menu_enbv', )
    fields = ('title', 'content', 'mode_page',  'un_menu_enbv', 'date_created', 'date_change')
    readonly_fields = ('date_change',)
    search_fields = ('title', 'date_created', 'date_change', 'un_menu_enbv', 'content')


admin.site.register(Content, ContentAdmin)
# admin.site.register(ModePage)
# admin.site.register(UnMenuENBVU)
# admin.site.register(PictureFile)




