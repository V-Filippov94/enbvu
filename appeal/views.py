from django.contrib import messages
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import *
from .forms import AppealHead
from index_enbvu.utils import DataMixin


class AppealHeadFormView(DataMixin, CreateView):
    model = AppealModel
    template_name = 'appeal/appeal_head.html'
    success_url = reverse_lazy('appeal:appeal_head')
    form_class = AppealHead

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Енисейское БВУ. Обращение к руководителю')
        return dict(list(context.items()) + list(user_context.items()))

    def form_valid(self, form):
        data = form.data
        subject = f'Сообщение от {data["name"]} Email отправителя: {data["email"]}'
        print(subject)
        messages.add_message(self.request, messages.SUCCESS, 'Сообщение успешно отправлено!')
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super(AppealHeadFormView, self).form_invalid(form)
        messages.error(self.request, 'Произошла ошибка, повторите попытку позже!')
        return response


class ShowInfoObrasheniya(DataMixin, ListView):
    model = ContentAppeal
    template_name = 'appeal/informaciya_o_rabote_s_grazhdanami.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_appeal'] = UnMenuAppeal.objects.filter(
            name='Информация о работе с обращениями граждан, организаций, общественных объединений, государственных'
                 ' органов, органов местного самоуправления')
        user_context = self.get_user_context(unMenuAppeal=context['menu_appeal'][:1],
                                             title='Енисейское БВУ. Информация о работе с обращениями граждан, '
                                                   'организаций, общественных объединений, государственных органов, '
                                                   'органов местного самоуправления')
        return dict(list(context.items()) + list(user_context.items()))

