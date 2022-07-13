from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class FunctionUpravAdminForm(forms.ModelForm):
    text_function = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model: FunctionUprav
        fields: '__all__'


class PolnomochiyaAdminForm(forms.ModelForm):
    text_polnomochiya = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model: Polnomochiya
        fields: '__all__'


class NormAktFunctionAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model: NormAktFunction
        fields: '__all__'


class InfoZakupkiAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model: InfoZakupki
        fields: '__all__'


class PlanProverokAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model: PlanProverok
        fields: '__all__'


class FunctionUpravAdmin(admin.ModelAdmin):
    form = FunctionUpravAdminForm
    list_display = ('id', 'text_function')
    list_display_links = ('id', 'text_function')


class PolnomochiyaAdmin(admin.ModelAdmin):
    form = PolnomochiyaAdminForm
    list_display = ('id', 'text_polnomochiya')
    list_display_links = ('id', 'text_polnomochiya')


class NormAktFunctionAdmin(admin.ModelAdmin):
    form = NormAktFunctionAdminForm
    list_display = ('title', 'file_pdf', 'date_created')
    list_display_links = ('title',)


class PhoneOrganizationInline(admin.TabularInline):
    model = PhoneOrganization


class SectorOrganizationInline(admin.TabularInline):
    model = SectorOrganization


class OrganizationAdmin(admin.ModelAdmin):
    inlines = [PhoneOrganizationInline, SectorOrganizationInline]
    list_display = ('name', 'email')
    fields = ('name', 'address', 'address_cor', 'mode', 'fax', 'email')
    readonly_fields = ('name',)


class PhoneWorkerInline(admin.TabularInline):
    model = PhoneWorker


class WorkerAdmin(admin.ModelAdmin):
    inlines = [PhoneWorkerInline]
    list_display = ('name', 'post', 'email')
    list_display_links = ('name', 'post')
    list_filter = ('post', 'organization', 'sector_organization')
    search_fields = ('post', 'organization', 'sector_organization', 'email')
    fields = ('name', 'post', 'organization', 'sector_organization', 'email')
    readonly_fields = ('post',)


class AddressUchrezhdeniyaInline(admin.TabularInline):
    model = AddressUchrezhdeniya


class PhoneUchrezhdeniyaInline(admin.TabularInline):
    model = PhoneUchrezhdeniya


class UchrezhdeniyaAdmin(admin.ModelAdmin):
    inlines = [AddressUchrezhdeniyaInline, PhoneUchrezhdeniyaInline]
    list_display = ('name', 'site')
    list_display_links = ('name', 'site')


class InfoZakupkiAdmin(admin.ModelAdmin):
    form = InfoZakupkiAdminForm
    list_display = ('title', 'date_created')
    list_display_links = ('title', 'date_created')


class PlanProverokAdmin(admin.ModelAdmin):
    form = PlanProverokAdminForm
    list_display = ('title',)


class OficialVystupAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_pdf')


class SvedeniyaSmiAdmin(admin.ModelAdmin):
    list_display = ('text',)


admin.site.register(FunctionUprav, FunctionUpravAdmin)
admin.site.register(Polnomochiya, PolnomochiyaAdmin)
admin.site.register(NormAktFunction, NormAktFunctionAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Uchrezhdeniya, UchrezhdeniyaAdmin)
admin.site.register(InfoZakupki, InfoZakupkiAdmin)
admin.site.register(PlanProverok, PlanProverokAdmin)
admin.site.register(OficialVystup, OficialVystupAdmin)
admin.site.register(SvedeniyaSmi, SvedeniyaSmiAdmin)



