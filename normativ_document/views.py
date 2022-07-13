from django.shortcuts import render
from django.views.generic import ListView
from index_enbvu.utils import DataMixin
from .models import *
from index_enbvu.models import NewsFiles


class NormAktRosvodres(DataMixin, ListView):
    model = NewsFiles
    context_object_name = 'uchrezhdeniya'
    template_name = 'enisey_bvu/podvedomstvennye-uchrezhdeniya.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        user_context = self.get_user_context(title='Енисейское БВУ. Подведомственные учреждения')
        return dict(list(context.items()) + list(user_context.items()))

