from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(), label='Текст Новости')

    class Meta:
        model: News
        fields: '__all__'


class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('id', 'title', 'url')
    list_display_links = ('title', 'url')


class UnMenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('title', 'url', 'cat')
    list_display_links = ('title', 'url')
    search_fields = ('title', 'url')
    list_filter = ('cat',)


class NewsImageInline(admin.TabularInline):
    model = NewsImage


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    inlines = [NewsImageInline]
    list_display = ('title', 'date_create', 'time_update', 'hot')
    list_display_links = ('title', 'date_create', 'time_update')
    search_fields = ('title', 'date_create', 'time_update')
    list_filter = ('date_create', 'time_update')
    fields = ('title', 'description', 'date_create', 'time_update', 'hot')
    readonly_fields = ('time_update', )


class PhotoLinkAdmin(admin.ModelAdmin):
    list_display = ('get_html_photo', 'url')
    list_display_links = ('get_html_photo', 'url')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="200">')
    get_html_photo.short_description = 'Фото ссылки'


class VeteranListAdmin(admin.ModelAdmin):
    list_display = ('photo', 'get_html_photo', 'date_created')
    list_display_links = ('photo', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="250">')
    get_html_photo.short_description = 'Фото'


class MirVodyImageInline(admin.TabularInline):
    model = MirVodyImage


class MirVodyYearAdmin(admin.ModelAdmin):
    inlines = [MirVodyImageInline]
    list_display = ('slug', 'date_created')
    list_display_links = ('slug', 'date_created')


admin.site.site_header = 'Енисейское БВУ'
admin.site.site_title = 'Енисейское БВУ'


# admin.site.register(Menu, MenuAdmin)
admin.site.register(News, NewsAdmin)
# admin.site.register(UnMenu, UnMenuAdmin)
admin.site.register(PhotoLink, PhotoLinkAdmin)
admin.site.register(VeteranList, VeteranListAdmin)
admin.site.register(MirVodyYear, MirVodyYearAdmin)




