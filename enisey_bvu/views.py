from django.views.generic import ListView
from index_enbvu.utils import DataMixin
from .models import *


class FunctionBVU(DataMixin, ListView):
    model = FunctionUprav
    context_object_name = 'list_func_uprav'
    template_name = 'enisey_bvu/function_bvu.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['polnomochiya'] = Polnomochiya.objects.all()
        user_context = self.get_user_context(title='Енисейское БВУ. Функции и полномочия')
        return dict(list(context.items()) + list(user_context.items()))


class NormativAktFunction(DataMixin, ListView):
    model = NormAktFunction
    context_object_name = 'normativ_akt_function_obj'
    template_name = 'enisey_bvu/normativ_akt_function.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(
            title='Енисейское БВУ. Нормативные акты, определяющие полномочия, задачи и функции'
        )
        return dict(list(context.items()) + list(user_context.items()))


class StrukturaUpravleniya(DataMixin, ListView):
    model = Worker
    context_object_name = 'workers'
    template_name = 'enisey_bvu/struktura_upravleniya.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_org'] = Organization.objects.filter(name="Енисейское БВУ")
        context['phone_org_first'] = PhoneOrganization.objects.filter(organization=context['first_org'][:1])

        context['boss'] = Worker.objects.filter(post='Руководитель управления')
        context['boss_phone'] = PhoneWorker.objects.filter(worker=context['boss'][:1])

        context['zam'] = Worker.objects.filter(post='Заместитель руководителя')
        context['workers_phone'] = PhoneWorker.objects.all()

        context['list_sector'] = SectorOrganization.objects.all()
        context['list_workers'] = Worker.objects.all()

        context['all_org'] = Organization.objects.all()
        context['phone_org'] = PhoneOrganization.objects.all()

        user_context = self.get_user_context(title='Енисейское БВУ. Структура управления')
        return dict(list(context.items()) + list(user_context.items()))


class PodvedomUchrezhdeniya(DataMixin, ListView):
    model = Uchrezhdeniya
    context_object_name = 'uchrezhdeniya'
    template_name = 'enisey_bvu/podvedomstvennye-uchrezhdeniya.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = AddressUchrezhdeniya.objects.all()
        context['phones'] = PhoneUchrezhdeniya.objects.all()
        user_context = self.get_user_context(title='Енисейское БВУ. Подведомственные учреждения')
        return dict(list(context.items()) + list(user_context.items()))


class PerechniInfoSistem(DataMixin, ListView):
    model = Uchrezhdeniya
    template_name = 'enisey_bvu/perechni_informacionnyh_sistem.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(
            title='Енисейское БВУ. Перечни информационных систем, баз данных, реестров, регистров')
        return dict(list(context.items()) + list(user_context.items()))


class InfoZakupok(DataMixin, ListView):
    model = InfoZakupki
    template_name = 'enisey_bvu/info_zakupki.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info_zakupki'] = InfoZakupki.objects.all()
        user_context = self.get_user_context(
            title='Енисейское БВУ. Информация об осуществлении закупок товаров, работ, услуг для государственных нужд')
        return dict(list(context.items()) + list(user_context.items()))


class PlanProverki(DataMixin, ListView):
    model = PlanProverok
    context_object_name = 'plan_proverok'
    template_name = 'enisey_bvu/plan_proverok.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plan_proverok'] = PlanProverok.objects.all()
        user_context = self.get_user_context(
            title='Енисейское БВУ. План проверок, результаты проверок')
        return dict(list(context.items()) + list(user_context.items()))


class OficialVystupleniya(DataMixin, ListView):
    model = OficialVystup
    context_object_name = 'oficial_vystupleniya'
    template_name = 'enisey_bvu/oficial_vystupleniya_zayavleniya.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(
            title='Енисейское БВУ.  Официальные выступления и заявления')
        return dict(list(context.items()) + list(user_context.items()))


class SvedeniyaOSmi(DataMixin, ListView):
    model = SvedeniyaSmi
    context_object_name = 'svedeniya_o_smi'
    template_name = 'enisey_bvu/svedeniya_o_smi.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(
            title='Енисейское БВУ.  Сведения о финансировании (отсутсвии финансирования) средств массовой информации')
        return dict(list(context.items()) + list(user_context.items()))