from django.views.generic import ListView
from index_enbvu.utils import DataMixin
from .models import *


class ShowPage(DataMixin, ListView):
    model = Content
    template_name = 'enisey_bvu/function_bvu.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = UnMenuENBVU.objects.filter(name='Функции и полномочия Енисейского БВУ')
        user_context = self.get_user_context(unMenuArg=context['menu'][:1], title='Енисейское БВУ. Функции и полномочия'
                                                                                  ' Енисейского БВУ')
        return dict(list(context.items()) + list(user_context.items()))


class ShowPageNormativAkt(DataMixin, ListView):
    model = ListFile
    template_name = 'enisey_bvu/normativ_akt_function.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = UnMenuENBVU.objects.filter(name='Нормативные акты, определяющие полномочия, задачи и функции')
        user_context = self.get_user_context(unMenuArg=context['menu'][:1], title='Енисейское БВУ. Нормативные акты, '
                                                                                  'определяющие полномочия, задачи и'
                                                                                  ' функции')
        return dict(list(context.items()) + list(user_context.items()))


class ShowPageStructure(DataMixin, ListView):
    model = Content
    template_name = 'enisey_bvu/struktura_upravleniya.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = UnMenuENBVU.objects.filter(name='Структура управления')
        user_context = self.get_user_context(unMenuArg=context['menu'][:1], title='Енисейское БВУ. Структура'
                                                                                  ' управления')
        return dict(list(context.items()) + list(user_context.items()))


class ShowPageContact(DataMixin, ListView):
    model = Content
    template_name = 'enisey_bvu/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = UnMenuENBVU.objects.filter(name='Контактные данные')
        user_context = self.get_user_context(unMenuArg=context['menu'][:1], title='Енисейское БВУ. Контактные данные')
        return dict(list(context.items()) + list(user_context.items()))


class ShowPageUchrezhdeniya(DataMixin, ListView):
    model = Content
    template_name = 'enisey_bvu/podved_uchrezhdeniya.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = UnMenuENBVU.objects.filter(name='Подведомственные учреждения')
        user_context = self.get_user_context( unMenuArg=context['menu'][:1], title='Енисейское БВУ. Подведомственные '
                                                                                   'учреждения')
        return dict(list(context.items()) + list(user_context.items()))


class ShowPagePerechniRegistr(DataMixin, ListView):
    model = Content
    template_name = 'enisey_bvu/perechni_info_sistem.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = UnMenuENBVU.objects.filter(name='Перечни информационных систем, банков данных, реестров,'
                                                          ' регистров')

        user_context = self.get_user_context(unMenuArg=context['menu'][:1], title='Енисейское БВУ. Перечни '
                                                                                  'информационных систем банков данных,'
                                                                                  ' реестров, регистров')
        return dict(list(context.items()) + list(user_context.items()))


class ShowPageInfoZakup(DataMixin, ListView):
    model = Content
    template_name = 'enisey_bvu/info_zakup.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = UnMenuENBVU.objects.filter(name='Осуществление закупок для государственных нужд')

        user_context = self.get_user_context(unMenuArg=context['menu'][:1],
                                             title=' Енисейское БВУ.Осуществление закупок для государственных нужд')
        return dict(list(context.items()) + list(user_context.items()))


class ShowPagePlanProverok(DataMixin, ListView):
    model = Content
    template_name = 'enisey_bvu/plan_proverok.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = UnMenuENBVU.objects.filter(name='План проверок, результаты проверок')

        user_context = self.get_user_context(unMenuArg=context['menu'][:1], title='Енисейское БВУ. '
                                                                                  'План проверок, результаты проверок')
        return dict(list(context.items()) + list(user_context.items()))


class ShowPageOficialVistup(DataMixin, ListView):
    model = Content
    template_name = 'enisey_bvu/oficial_vistupleniya.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = UnMenuENBVU.objects.filter(name='Официальные выступления и заявления')

        user_context = self.get_user_context(unMenuArg=context['menu'][:1], title='Енисейское БВУ. Официальные '
                                                                                  'выступления и заявления')
        return dict(list(context.items()) + list(user_context.items()))


class ShowPageInfoFinance(DataMixin, ListView):
    model = Content
    template_name = 'enisey_bvu/svedeniya_o_finansirovanii.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = UnMenuENBVU.objects.filter(name='Сведения о финансировании (отсутсвии финансирования) '
                                                      'средств массовой информации')

        user_context = self.get_user_context(unMenuArg=context['menu'][:1], title='Енисейское БВУ. '
                                                                                  'Сведения о финансировании средств'
                                                                                  ' массовой информации')
        return dict(list(context.items()) + list(user_context.items()))
