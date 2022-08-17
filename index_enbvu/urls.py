from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', BasePage.as_view(), name='base_page'),
    path('enisejskoe-bvu/enbvu_news/', NewsPage.as_view(), name='news_page'),
    path('veteran_2020/', Veteran.as_view(), name='veteran_page'),
    path('mir_vody/', ShowListMirVody.as_view(), name='mir_vody_list'),
    path('mir_vody/<slug:mir_vody_slug>/', ShowMirVody.as_view(), name='mir_vody'),
    path('search/', SearchResultsView.as_view(), name='search_results_view'),
    path('map/', ShowMap.as_view(), name='map')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
