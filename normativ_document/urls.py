from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'normativ_document'

urlpatterns = [
    path('normativnye-pravovye-akty-izdannye-rosvodresursami/', ShowNormAkt.as_view(), name='norm_pravovye_akty'),
    path('administrativnye-reglamenty-standarty-gosudarstvennyh-uslug/', ShowAdminReg.as_view(), name='admin_reg'),
    path('ustanovlennye-formy-obrashenij-zayavlenij-i-inyh-dokumentov/', ShowUstanovFormy.as_view(),
         name='ustanov_formy'),
    path('poryadok-obzhalovaniya/', ShowPoryadokObzhalovaniya.as_view(), name='poryadok_obzhalovaniya'),
    path('formy-gosudarstvennoj-otchetnosti/', ShowFormyGosotchet.as_view(), name='formy_gos_otchetnosti'),
    path('pravila-obrabotki-personalnyh-dannyh/', ShowPravilaObrabotki.as_view(), name='pravila_obrabotki'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
