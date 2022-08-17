from django.views.generic import ListView
from index_enbvu.utils import DataMixin

from .models import *


class ShowNormAkt(DataMixin, ListView):
    model = ContentNormAkt
    template_name = 'normativ_document/normativ_akt.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_norm_akt'] = UnMenuNormAkt.objects.filter(
            name='Нормативные правовые акты, изданные Росводресурсами')
        user_context = self.get_user_context(unMenuNormAkt=context['menu_norm_akt'][:1],
                                             title='Енисейское БВУ. Нормативные правовые акты, изданные '
                                                   'Росводресурсами')
        return dict(list(context.items()) + list(user_context.items()))


class ShowAdminReg(DataMixin, ListView):
    model = ContentNormAkt
    template_name = 'normativ_document/admin_reg.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_norm_akt'] = UnMenuNormAkt.objects.filter(
            name='Административные регламенты, стандарты государственных услуг')
        user_context = self.get_user_context(unMenuNormAkt=context['menu_norm_akt'][:1],
                                             title='Енисейское БВУ. Административные регламенты, стандарты '
                                                   'государственных услуг')
        return dict(list(context.items()) + list(user_context.items()))


class ShowUstanovFormy(DataMixin, ListView):
    model = ContentNormAkt
    template_name = 'normativ_document/ustanov_formy.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_norm_akt'] = UnMenuNormAkt.objects.filter(
            name='Установленные формы обращений, заявлений и иных документов')
        user_context = self.get_user_context(unMenuNormAkt=context['menu_norm_akt'][:1],
                                             title='Енисейское БВУ. Установленные формы обращений, заявлений и иных '
                                                   'документов')
        return dict(list(context.items()) + list(user_context.items()))


class ShowPoryadokObzhalovaniya(DataMixin, ListView):
    model = ContentNormAkt
    template_name = 'normativ_document/poryadok_obzhalovaniya.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_norm_akt'] = UnMenuNormAkt.objects.filter(
            name='Порядок обжалования нормативных правовых актов и иных решений')
        user_context = self.get_user_context(unMenuNormAkt=context['menu_norm_akt'][:1],
                                             title='Енисейское БВУ. Порядок обжалования нормативных правовых актов '
                                                   'и иных решений')
        return dict(list(context.items()) + list(user_context.items()))


class ShowFormyGosotchet(DataMixin, ListView):
    model = ContentNormAkt
    template_name = 'normativ_document/formy_gos_otchetnosti.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_norm_akt'] = UnMenuNormAkt.objects.filter(
            name='Формы государственной статистической отчетности №2-тп (водхоз), №2-ОС')
        user_context = self.get_user_context(unMenuNormAkt=context['menu_norm_akt'][:1],
                                             title='Енисейское БВУ. Формы государственной статистической '
                                                   'отчетности №2-тп (водхоз), №2-ОС')
        return dict(list(context.items()) + list(user_context.items()))


class ShowPravilaObrabotki(DataMixin, ListView):
    model = ContentNormAkt
    template_name = 'normativ_document/pravila_obrabotki.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_norm_akt'] = UnMenuNormAkt.objects.filter(
            name='Правила обработки персональных данных в Енисейском БВУ (документ, определяющий политику '
                 'Енисейского БВУ в отношении обработки персональных данных)')
        user_context = self.get_user_context(unMenuNormAkt=context['menu_norm_akt'][:1],
                                             title='Енисейское БВУ. Правила обработки персональных данных в '
                                                   'Енисейском БВУ (документ, определяющий политику Енисейского БВУ в'
                                                   ' отношении обработки персональных данных)')
        return dict(list(context.items()) + list(user_context.items()))