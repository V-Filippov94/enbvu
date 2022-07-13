from django.views.generic import ListView, DetailView
from .models import *
from .utils import DataMixin


class BasePage(DataMixin, ListView):
    model = News
    template_name = 'index_enbvu/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_news'] = News.objects.all().order_by('-date_create')[:1]
        context['all_news'] = News.objects.all().order_by('-date_create')[:7]
        context['image'] = NewsImage.objects.filter(news=context['first_news'])
        context['pdf'] = NewsFilePDF.objects.filter(news_pdf=context['first_news'])
        context['file'] = NewsFiles.objects.filter(news_file=context['first_news'])

        user_context = self.get_user_context(title='Енисейское БВУ')
        return dict(list(context.items()) + list(user_context.items()))


class NewsPage(DataMixin, ListView):
    model = News
    template_name = 'index_enbvu/news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['img'] = NewsImage.objects.all()
        context['all_pdf'] = NewsFilePDF.objects.all()
        context['all_files'] = NewsFiles.objects.all()

        user_context = self.get_user_context(title='Новости ЕнБВУ')
        return dict(list(context.items()) + list(user_context.items()))


class Veteran(DataMixin, ListView):
    model = VeteranList
    template_name = 'index_enbvu/veteran_2020.html'
    context_object_name = 'veterans'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Енисейское БВУ. Фотогалерея воинской славы. Бессмертный полк-2020')
        return dict(list(context.items()) + list(user_context.items()))


class ShowListMirVody(DataMixin, ListView):
    model = MirVodyYear
    template_name = 'index_enbvu/mir_vody.html'
    context_object_name = 'mir_vody_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mir_vody_last'] = MirVodyImage.objects.all()
        context['mir_vody_year_last'] = MirVodyYear.objects.all().last()
        user_context = self.get_user_context(title='Енисейское БВУ. Выставка детского рисунка "Мир Воды"')
        return dict(list(context.items()) + list(user_context.items()))


class ShowMirVody(DataMixin, DetailView):
    model = MirVodyYear
    template_name = 'index_enbvu/mir_vody_detail.html'
    context_object_name = 'mir_vody'
    slug_url_kwarg = 'mir_vody_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mir_vody_list'] = MirVodyYear.objects.all().order_by('date_created')
        context['image_mir_vody'] = MirVodyImage.objects.all()
        user_context = self.get_user_context(title='Енисейское БВУ. Выставка детского рисунка "Мир Воды"')
        return dict(list(context.items()) + list(user_context.items()))

