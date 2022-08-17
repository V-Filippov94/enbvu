from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import *
from .utils import DataMixin

from appeal.models import ContentAppeal, ListFileAppeal
from corruption.models import ContentCorruption, ListFileCorruption
from deyatelnost.models import ContentDeyatelnost, ListFileDeyatelnost, VodHoz, PrikazOZonePodtop, \
    ListFilePrikazOZonePodtop
from enisey_bvu.models import Content, ListFile
from kadr_provision.models import KadrProvision, ListFileKadr, UnPageKadr
from normativ_document.models import ContentNormAkt, ListFileNormAkt
from okazanie_gosuslug.models import ContentOkazanieGosuslug, ListFileOkazanieGosuslug


class BasePage(DataMixin, ListView):
    model = News
    template_name = 'index_enbvu/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_news'] = News.objects.all().order_by('-date_create')[:1]
        context['all_news'] = News.objects.all().order_by('-date_create')[:7]
        context['hot_news'] = News.objects.filter(hot=True)
        context['hot_image'] = NewsImage.objects.all()
        context['image'] = NewsImage.objects.filter(news=context['first_news'])
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


class SearchResultsView(DataMixin, ListView):
    model = News
    template_name = 'index_enbvu/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = News.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

        obj_list_enisey_bvu = Content.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        obj_list_poyasneniya_file_enbvu = ListFile.objects.filter(Q(text__icontains=query))
        obj_list_enisey_bvu_all = Content.objects.all()  # для поиска ссылки на list_file

        obj_list_norm_doc = ContentNormAkt.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        obj_list_poyasneniya_file_norm_doc = ListFileNormAkt.objects.filter(Q(text__icontains=query))
        obj_list_norm_doc_all_cont = ContentNormAkt.objects.all()

        obj_list_deyatelnost = ContentDeyatelnost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query))
        obj_list_poyasneniya_file_deyatelnost = ListFileDeyatelnost.objects.filter(Q(text__icontains=query))
        obj_list_deyatelnost_all_cont = ContentDeyatelnost.objects.all()

        obj_list_vod_hoz = VodHoz.objects.filter(Q(sayno_sush__icontains=query) | Q(maiynskoe__icontains=query) |
                                                 Q(kras__icontains=query) | Q(irk__icontains=query) |
                                                 Q(bratsk__icontains=query) | Q(ust_ilim__icontains=query) |
                                                 Q(boguch__icontains=query))

        obj_list_district = PrikazOZonePodtop.objects.filter(Q(district__icontains=query))
        obj_list_poyasneniya_zone_podtop = ListFilePrikazOZonePodtop.objects.filter(Q(text__icontains=query))

        obj_list_kadr_provision = KadrProvision.objects.filter(
            Q(title__icontains=query) | Q(content_kadr__icontains=query))
        obj_list_poyasneniya_kadr = ListFileKadr.objects.filter(Q(text__icontains=query))
        obj_list_kar_all = KadrProvision.objects.all()

        obj_list_gosuslugi = ContentOkazanieGosuslug.objects.filter(
            Q(title__icontains=query) | Q(content_okazanie_gosuslug__icontains=query))
        obj_list_poyasneniya_gosuslugi = ListFileOkazanieGosuslug.objects.filter(Q(text__icontains=query))
        obj_list_gosuslugi_all = ContentOkazanieGosuslug.objects.all()

        obj_list_appeal = ContentAppeal.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
        obj_list_poyasneniya_appeal = ListFileAppeal.objects.filter(Q(text__icontains=query))
        obj_list_appeal_all = ContentAppeal.objects.all()

        obj_list_corrupt = ContentCorruption.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
        obj_list_poyasneniya_corrupt = ListFileCorruption.objects.filter(Q(text__icontains=query))
        obj_list_corrupt_all = ContentCorruption.objects.all()

        if query:
            return object_list, obj_list_enisey_bvu, obj_list_poyasneniya_file_enbvu, obj_list_enisey_bvu_all, \
                   obj_list_norm_doc, obj_list_poyasneniya_file_norm_doc, obj_list_norm_doc_all_cont, \
                   obj_list_deyatelnost, obj_list_poyasneniya_file_deyatelnost, obj_list_deyatelnost_all_cont, \
                   obj_list_vod_hoz, obj_list_district, obj_list_poyasneniya_zone_podtop, obj_list_kadr_provision, \
                   obj_list_poyasneniya_kadr, obj_list_kar_all, obj_list_gosuslugi, obj_list_poyasneniya_gosuslugi, \
                   obj_list_gosuslugi_all, obj_list_appeal, obj_list_poyasneniya_appeal, obj_list_appeal_all, \
                   obj_list_corrupt, obj_list_poyasneniya_corrupt, obj_list_corrupt_all

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Енисейское БВУ. Поиск')
        return dict(list(context.items()) + list(user_context.items()))


class ShowMap(DataMixin, ListView):
    model = Menu
    template_name = 'index_enbvu/map.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_menu'] = Menu.objects.all()
        context['list_un_menu'] = UnMenu.objects.all()
        context['list_kadr'] = UnPageKadr.objects.all()
        user_context = self.get_user_context(title='Енисейское БВУ. Карта сайта')
        return dict(list(context.items()) + list(user_context.items()))