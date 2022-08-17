from django.contrib import messages
from django.views.generic import ListView, CreateView, TemplateView
from index_enbvu.utils import DataMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import *
from .forms import AppealAniCor


class ShowAktyAntiCorruption(DataMixin, ListView):
    model = ContentCorruption
    template_name = 'corruption/akty_anti_corruption.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_corruption'] = UnMenuCorruption.objects.filter(name='Нормативные правовые и иные акты в сфере'
                                                                           ' противодействия коррупции')
        user_context = self.get_user_context(unMenuCorrution=context['menu_corruption'][:1],
                                             title='Енисейское БВУ. Нормативные правовые и иные акты в сфере'
                                                   ' противодействия коррупции')
        return dict(list(context.items()) + list(user_context.items()))


class ShowAntiKorEkspertiza(DataMixin, ListView):
    model = ContentCorruption
    template_name = 'corruption/antikorrupcionnaya_ekspertiza.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_corruption'] = UnMenuCorruption.objects.filter(name='Антикоррупционная экспертиза')
        user_context = self.get_user_context(unMenuCorrution=context['menu_corruption'][:1],
                                             title='Енисейское БВУ. Антикоррупционная экспертиза')
        return dict(list(context.items()) + list(user_context.items()))


class ShowMetodiMaterial(DataMixin, ListView):
    model = ContentCorruption
    template_name = 'corruption/metodicheskie_materialy.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_corruption'] = UnMenuCorruption.objects.filter(name='Методические материалы')
        user_context = self.get_user_context(unMenuCorrution=context['menu_corruption'][:1],
                                             title='Енисейское БВУ.	Методические материалы')
        return dict(list(context.items()) + list(user_context.items()))


class ShowDocAntiCor(DataMixin, ListView):
    model = ContentCorruption
    template_name = 'corruption/doc_anti_cor.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_corruption'] = UnMenuCorruption.objects.filter(name='Формы документов, связанных с '
                                                                          'противодействием коррупции, для заполнения')
        user_context = self.get_user_context(unMenuCorrution=context['menu_corruption'][:1],
                                             title='Енисейское БВУ.	Формы документов, связанных с противодействием'
                                                   ' коррупции, для заполнения')
        return dict(list(context.items()) + list(user_context.items()))


class ShowSvedeniyaODohodah(DataMixin, ListView):
    model = ContentCorruption
    template_name = 'corruption/svedeniya_o_dohodah.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_corruption'] = UnMenuCorruption.objects.filter(name='Сведения о доходах, расходах, об имуществе'
                                                                          ' и обязательствах имущественного характера')
        user_context = self.get_user_context(unMenuCorrution=context['menu_corruption'][:1],
                                             title='Енисейское БВУ.Сведения о доходах, расходах, об имуществе и '
                                                   'обязательствах имущественного характера')
        return dict(list(context.items()) + list(user_context.items()))


class ShowKomissiya(DataMixin, ListView):
    model = ContentCorruption
    template_name = 'corruption/komissiya.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_corruption'] = UnMenuCorruption.objects.filter(name='Комиссия по соблюдению требований к '
                                                                          'служебному поведению и урегулированию '
                                                                          'конфликта интересов (аттестационная '
                                                                          'комиссия)')
        user_context = self.get_user_context(unMenuCorrution=context['menu_corruption'][:1],
                                             title='Енисейское БВУ.Комиссия по соблюдению требований к служебному'
                                                   ' поведению и урегулированию конфликта интересов (аттестационная'
                                                   ' комиссия)')
        return dict(list(context.items()) + list(user_context.items()))


class ShowLinkAntiCor(DataMixin, CreateView):
    model = ContentCorruption
    form_class = AppealAniCor
    template_name = 'corruption/obratnaya_svyaz.html'
    success_url = reverse_lazy('corruption:obratnaya_svyaz')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_corruption'] = UnMenuCorruption.objects.filter(name='Обратная связь для сообщений о фактах '
                                                                          'коррупции')
        user_context = self.get_user_context(unMenuCorrution=context['menu_corruption'][:1],
                                             title='Енисейское БВУ.Обратная связь для сообщений о фактах коррупции')
        return dict(list(context.items()) + list(user_context.items()))

    def form_valid(self, form):
        form_save = form.save()
        data = form.data
        print(data)
        messages.add_message(self.request, messages.SUCCESS, 'Ваше сообщение успешно отправлено')
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super(ShowLinkAntiCor, self).form_invalid(form)
        messages.error(self.request, 'Ошибка отправки сообщения, повторите попытку позже')
        return response


class ShowDokladObzor(DataMixin, ListView):
    model = ContentCorruption
    template_name = 'corruption/doklady_otchety_obzory.html'

    def post(self, request, *args, **kwargs):
        update_type = request.POST.get('update_type')
        if 'add' in request.POST:
            if update_type == 'high':
                RatingWork.objects.create(high=True, average=False, short=False)
            elif update_type == 'average':
                RatingWork.objects.create(high=False, average=True, short=False)
            elif update_type == 'short':
                RatingWork.objects.create(high=False, average=False, short=True)

        return HttpResponseRedirect(self.request.path_info)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_corruption'] = UnMenuCorruption.objects.filter(name='Доклады, отчеты, обзоры, статистическая'
                                                                          ' информация')
        context['result_high'] = len(RatingWork.objects.filter(high=True))
        context['result_average'] = len(RatingWork.objects.filter(average=True))
        context['result_short'] = len(RatingWork.objects.filter(short=True))

        user_context = self.get_user_context(unMenuCorrution=context['menu_corruption'][:1],
                                             title='Енисейское БВУ. Доклады, отчеты, обзоры, статистическая информация')
        return dict(list(context.items()) + list(user_context.items()))


class ShowFAQ(DataMixin, ListView):
    model = ContentCorruption
    template_name = 'corruption/faq.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_corruption'] = UnMenuCorruption.objects.filter(name='Часто задаваемые вопросы')
        user_context = self.get_user_context(unMenuCorrution=context['menu_corruption'][:1],
                                             title='Енисейское БВУ. Часто задаваемые вопросы')
        return dict(list(context.items()) + list(user_context.items()))