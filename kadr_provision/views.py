from django.views.generic import ListView
from index_enbvu.utils import DataMixin
from .models import *


class ShowPorydokpostupleniya(DataMixin, ListView):
    model = KadrProvision
    template_name = 'kadr_provosion/poryadok_postupleniya.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_kadr'] = UnPageKadr.objects.filter(name='Порядок поступления граждан на государственную службу')

        user_context = self.get_user_context(unPageKadr=context['menu_kadr'][:1],
                                             title='Енисейское БВУ. Порядок поступления граждан на государственную'
                                                   ' службу')

        return dict(list(context.items()) + list(user_context.items()))


class ShowSvedeniyaVakansii(DataMixin, ListView):
    model = KadrProvision
    template_name = 'kadr_provosion/svedeniya_o_dolzhnostyah.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_kadr'] = UnPageKadr.objects.filter(name='Сведения о вакантных должностях и квалификационные'
                                                              ' требования к кандидатам на замещение вакантных '
                                                              'должностей')

        user_context = self.get_user_context(unPageKadr=context['menu_kadr'][:1],
                                             title='Енисейское БВУ. Сведения о вакантных должностях и квалификационные '
                                                   'требования к кандидатам на замещение вакантных должностей')
        return dict(list(context.items()) + list(user_context.items()))


class ShowResultKonkurs(DataMixin, ListView):
    model = KadrProvision
    template_name = 'kadr_provosion/result_konkurs.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_kadr'] = UnPageKadr.objects.filter(name='Результаты конкурсов на замещение вакантных должностей')

        user_context = self.get_user_context(unPageKadr=context['menu_kadr'][:1],
                                             title='Енисейское БВУ. Результаты конкурсов на замещение вакантных '
                                                   'должностей')
        return dict(list(context.items()) + list(user_context.items()))


class ShowContactPoVakansiyam(DataMixin, ListView):
    model = KadrProvision
    template_name = 'kadr_provosion/kontakty_po_voprosu_zamesheniya.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_kadr'] = UnPageKadr.objects.filter(name='Контактные данные по вопросу замещения вакантных'
                                                              ' должностей')

        user_context = self.get_user_context(unPageKadr=context['menu_kadr'][:1],
                                             title='Енисейское БВУ. Контактные данные по вопросу замещения вакантных '
                                                   'должностей')
        return dict(list(context.items()) + list(user_context.items()))


class ShowSostavKomissii(DataMixin, ListView):
    model = KadrProvision
    template_name = 'kadr_provosion/sostav_komissii.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_kadr'] = UnPageKadr.objects.filter(name='Состав комиссии по организации и проведению конкурсов '
                                                              'на замещение вакантных должностей')

        user_context = self.get_user_context(unPageKadr=context['menu_kadr'][:1],
                                             title='Енисейское БВУ. Состав комиссии по организации и проведению '
                                                   'конкурсов на замещение вакантных должностей')
        return dict(list(context.items()) + list(user_context.items()))


class ShowObzhalovanieResult(DataMixin, ListView):
    model = KadrProvision
    template_name = 'kadr_provosion/obzhalovanie_result.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_kadr'] = UnPageKadr.objects.filter(name='Порядок обжалования результатов конкурса')

        user_context = self.get_user_context(unPageKadr=context['menu_kadr'][:1],
                                             title='Енисейское БВУ. Порядок обжалования результатов конкурса')
        return dict(list(context.items()) + list(user_context.items()))