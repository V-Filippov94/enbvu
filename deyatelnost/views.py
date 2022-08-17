from django.db.models import Q
from django.views.generic import ListView
from index_enbvu.utils import DataMixin

from .models import *


class ShowUchastieVProgram(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/uchastie_v_program.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(name='Участие в целевых и иных программах')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Участие в целевых и иных программах')
        return dict(list(context.items()) + list(user_context.items()))


class ShowSotrudnichestvo(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/mezhdunarodnoe_sotrudnichestvo.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(name='Международное сотрудничество')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Международное сотрудничество')
        return dict(list(context.items()) + list(user_context.items()))


class ShowVystavki(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/kongressy_vystavki.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(
            name='Конгрессы, конференции, семинары, выставки')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Конгрессы, конференции, семинары, выставки')
        return dict(list(context.items()) + list(user_context.items()))


class ShowZashita(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/sostoyanie_zashity.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(
            name='Состояние защиты населения и территорий от чрезвычайных ситуаций')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Состояние защиты населения и территорий от '
                                                   'чрезвычайных ситуаций')
        return dict(list(context.items()) + list(user_context.items()))


class ShowStatistika(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/statisticheskie_dannye.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(name='Статистические данные и показатели')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Статистические данные и показатели')
        return dict(list(context.items()) + list(user_context.items()))


class ShowIspolzovaniSredstv(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/ispolzovanie_sredstv.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(
            name='Использование выделяемых бюджетных средств')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Использование выделяемых бюджетных средств')
        return dict(list(context.items()) + list(user_context.items()))


class ShowVodHoz(DataMixin, ListView):
    model = VodHoz
    template_name = 'deyatelnost/vodohozyajstvennaya_obstanovka.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vod_hoz'] = VodHoz.objects.all().first()
        user_context = self.get_user_context(title='Енисейское БВУ. Водохозяйственная обстановка')
        return dict(list(context.items()) + list(user_context.items()))


class ShowDateVodHoz(DataMixin, ListView):
    model = VodHoz
    template_name = 'deyatelnost/date_search_vod_hoz.html'

    def get_queryset(self):
        query = self.request.GET.get('Date')
        object_list = VodHoz.objects.filter(Q(date_created__icontains=query))
        return object_list, query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Енисейское БВУ. Поиск')
        return dict(list(context.items()) + list(user_context.items()))


class ShowVodnieObject(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/predostavlenie_vodnyh_obektov.html'
    ordering = ['date_change']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(
            name='Предоставление водных объектов в пользование')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Предоставление водных объектов в пользование')
        return dict(list(context.items()) + list(user_context.items()))


class ShowVodHozMeropriyatiya(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/vodohozyajstvennye_meropriyatiya.html'
    ordering = ['date_change']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(
            name='Водохозяйственные мероприятия')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Водохозяйственные мероприятия')
        return dict(list(context.items()) + list(user_context.items()))


class ShowMonitoring(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/monitoring_vodnyh_obektov.html'
    ordering = ['date_change']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(
            name='Мониторинг водных объектов')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Мониторинг водных объектов')
        return dict(list(context.items()) + list(user_context.items()))


class ShowBassSovet(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/bassejnovye_sovety.html'
    ordering = ['date_change']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(
            name='Бассейновые советы')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Бассейновые советы')
        return dict(list(context.items()) + list(user_context.items()))


class ShowUstanovRezhim(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/ustanovlenie_rezhimov.html'
    ordering = ['date_change']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(
            name='Установление режимов водохранилищ')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Установление режимов водохранилищ')
        return dict(list(context.items()) + list(user_context.items()))


class ShowSkiovo(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/skiovo_i_ndv.html'
    ordering = ['date_change']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(
            name='СКИОВО и НДВ')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. СКИОВО и НДВ')
        return dict(list(context.items()) + list(user_context.items()))


class ShowKadr(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/kadry.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(
            name='Кадровое обеспечение')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Кадровое обеспечение')
        return dict(list(context.items()) + list(user_context.items()))


class ShowSvedeniyaOLgotah(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/svedeniya_o_predostavlenii_lgot.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(
            name='Сведения о предоставлении льгот, отсрочек, рассрочках, о списании задолженности по платежам')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Сведения о предоставлении льгот, отсрочек,'
                                                   ' рассрочках, о списании задолженности по платежам')
        return dict(list(context.items()) + list(user_context.items()))


class ShowGraniciPodtop(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/opredelenie_granic_zatopleniya.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(
            name='Определение границ зон затопления, подтопления')
        context['region'] = Region.objects.all()
        context['district'] = PrikazOZonePodtop.objects.all()
        context['list_file'] = ListFilePrikazOZonePodtop.objects.all()
        context['files_podtop'] = FilePrikazOZonePodtop.objects.all()
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Определение границ зон затопления, подтопления')
        return dict(list(context.items()) + list(user_context.items()))


class ShowChSIrk(DataMixin, ListView):
    model = ContentDeyatelnost
    template_name = 'deyatelnost/likvidaciya_chs.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_deyatelnost'] = UnMenuDeyatelnost.objects.filter(name='Ликвидация ЧС в Иркутской области')
        user_context = self.get_user_context(unMenuDeyatelnost=context['menu_deyatelnost'][:1],
                                             title='Енисейское БВУ. Ликвидация ЧС в Иркутской области')
        return dict(list(context.items()) + list(user_context.items()))