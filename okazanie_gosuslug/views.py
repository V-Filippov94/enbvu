from django.views.generic import ListView
from index_enbvu.utils import DataMixin

from .models import *


class ShowSvedeniyaGosReestr(DataMixin, ListView):
    model = ContentOkazanieGosuslug
    template_name = 'okazanie_gosuslug/svedenia_gosreestr.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_okazanie_gosuslug'] = UnMenuOkazanieGosuslug.objects.filter(
            name='Предоставление сведений из государственного водного реестра и копий документов, содержащих сведения,'
                 ' включенные в государственный водный реестр')
        user_context = self.get_user_context(unMenuOkazanieGosuslug=context['menu_okazanie_gosuslug'][:1],
                                             title='Енисейское БВУ. Предоставление сведений из государственного водного'
                                                   ' реестра и копий документов, содержащих сведения, включенные в '
                                                   'государственный водный реестр')
        return dict(list(context.items()) + list(user_context.items()))


class ShowPolzovanieVodObject(DataMixin, ListView):
    model = ContentOkazanieGosuslug
    template_name = 'okazanie_gosuslug/polzovanie_vod_object.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_okazanie_gosuslug'] = UnMenuOkazanieGosuslug.objects.filter(
            name='Предоставление водных объектов в пользование на основании договора водопользования, в том числе '
                 'заключенного по результатам аукциона, по оформлению перехода прав и обязанностей по договорам '
                 'водопользования')
        user_context = self.get_user_context(unMenuOkazanieGosuslug=context['menu_okazanie_gosuslug'][:1],
                                             title='Енисейское БВУ. Предоставление водных объектов в пользование на '
                                                   'основании договора водопользования, в том числе заключенного по '
                                                   'результатам аукциона, по оформлению перехода прав и обязанностей '
                                                   'по договорам водопользования')
        return dict(list(context.items()) + list(user_context.items()))


class ShowPredostavVPolz(DataMixin, ListView):
    model = ContentOkazanieGosuslug
    template_name = 'okazanie_gosuslug/predostavlenie_v_polzovanie.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_okazanie_gosuslug'] = UnMenuOkazanieGosuslug.objects.filter(
            name='Предоставление права пользования водными объектами на основании решения о предоставлении водных'
                 ' объектов в пользование')
        user_context = self.get_user_context(unMenuOkazanieGosuslug=context['menu_okazanie_gosuslug'][:1],
                                             title='Енисейское БВУ. Предоставление права пользования водными объектами'
                                                   ' на основании решения о предоставлении водных объектов в'
                                                   ' пользование')
        return dict(list(context.items()) + list(user_context.items()))


class ShowUtverzhdenieSbrosov(DataMixin, ListView):
    model = ContentOkazanieGosuslug
    template_name = 'okazanie_gosuslug/utverzhdenie_sbrosov.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_okazanie_gosuslug'] = UnMenuOkazanieGosuslug.objects.filter(
            name='Утверждение нормативов допустимых сбросов веществ и микроорганизмов в водные объекты для в'
                 'одопользователей')
        user_context = self.get_user_context(unMenuOkazanieGosuslug=context['menu_okazanie_gosuslug'][:1],
                                             title='Енисейское БВУ. Утверждение нормативов допустимых сбросов веществ'
                                                   ' и микроорганизмов в водные объекты для водопользователей')
        return dict(list(context.items()) + list(user_context.items()))


class ShowZemUchastok(DataMixin, ListView):
    model = ContentOkazanieGosuslug
    template_name = 'okazanie_gosuslug/razresheniya_zemelnogo_uchastka.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_okazanie_gosuslug'] = UnMenuOkazanieGosuslug.objects.filter(
            name='Выдача разрешения на создание искусственного земельного участка на водном объекте')
        user_context = self.get_user_context(unMenuOkazanieGosuslug=context['menu_okazanie_gosuslug'][:1],
                                             title='Енисейское БВУ. Выдача разрешения на создание искусственного '
                                                   'земельного участка на водном объекте')
        return dict(list(context.items()) + list(user_context.items()))