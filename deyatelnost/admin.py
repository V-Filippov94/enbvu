from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class ContentDeyatelnostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Контент')

    class Meta:
        model: ContentDeyatelnost
        fields: '__all__'


class ListFileDeyatelnostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Контент')

    class Meta:
        model: ContentDeyatelnost
        fields: '__all__'


class ListFileDeyatelnostInline(admin.TabularInline):
    form = ListFileDeyatelnostAdminForm
    model = ListFileDeyatelnost

    def get_extra(self, request, obj=None, **kwargs):
        return 1 if obj else 3


class FileDeyatelnostInline(admin.TabularInline):
    model = FileDeyatelnost


class ContentDeyatelnostAdmin(admin.ModelAdmin):
    form = ContentDeyatelnostAdminForm
    inlines = [ListFileDeyatelnostInline, FileDeyatelnostInline]
    list_display = ('title', 'un_menu_deyatelnost', 'date_change')
    list_display_links = ('title', 'un_menu_deyatelnost')
    list_filter = ('date_change', 'un_menu_deyatelnost')
    fields = ('title', 'content', 'mode_page', 'un_menu_deyatelnost', 'date_created', 'date_change')
    readonly_fields = ('date_change',)
    search_fields = ('title', 'date_created', 'date_change', 'un_menu_deyatelnost', 'content')


class VodHozAdmin(admin.ModelAdmin):
    list_display = ('date_created',)
    list_filter = ('date_created',)
    search_fields = ('date_created',)
    fields = ('sayno_sush', 'maiynskoe', 'kras', 'irk', 'bratsk', 'ust_ilim', 'boguch', 'date_created', 'date_change')
    readonly_fields = ('date_change',)


class ListFilePrikazOZonePodtopAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Контент')

    class Meta:
        model: ListFilePrikazOZonePodtop
        fields: '__all__'


class ListFilePrikazOZonePodtopInline(admin.TabularInline):
    form = ListFilePrikazOZonePodtopAdminForm
    model = ListFilePrikazOZonePodtop

    def get_extra(self, request, obj=None, **kwargs):
        return 1 if obj else 3


class FilePrikazOZonePodtopInline(admin.TabularInline):
    model = FilePrikazOZonePodtop


class PrikazOZonePodtopAdmin(admin.ModelAdmin):
    inlines = [ListFilePrikazOZonePodtopInline, FilePrikazOZonePodtopInline]
    list_display = ('district', 'region', 'date_created')
    list_filter = ('date_created', 'region')
    fields = ('district', 'region', 'date_created', 'date_change')
    readonly_fields = ('date_change',)


admin.site.register(ContentDeyatelnost, ContentDeyatelnostAdmin)
admin.site.register(VodHoz, VodHozAdmin)
# admin.site.register(UnMenuDeyatelnost)
# admin.site.register(Region)
admin.site.register(PrikazOZonePodtop, PrikazOZonePodtopAdmin)
