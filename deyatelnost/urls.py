from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'deyatelnost'

urlpatterns = [
    path('uchastie-v-celevyh-i-inyh-programmah/', ShowUchastieVProgram.as_view(), name='uchastie_v_program'),
    path('mezhdunarodnoe-sotrudnichestvo/', ShowSotrudnichestvo.as_view(), name='mezhdunarodnoe_sotrudnichestvo'),
    path('kongressy-konferencii-seminary-vystavki/', ShowVystavki.as_view(), name='kongressy_vystavki'),
    path('sostoyanie-zashity-ot-chrezvychajnyh-situacij/', ShowZashita.as_view(), name='sostoyanie_zashity'),
    path('statisticheskie-dannye-i-pokazateli/', ShowStatistika.as_view(), name='statisticheskie_dannye'),
    path('ispolzovanie-vydelyaemyh-byudzhetnyh-sredstv/', ShowIspolzovaniSredstv.as_view(),
         name='ispolzovanie_sredstv'),
    path('vodohozyajstvennaya-obstanovka/', ShowVodHoz.as_view(), name='vodohozyajstvennaya_obstanovka'),
    path('vodohozyajstvennaya-obstanovka/date_search/', ShowDateVodHoz.as_view(), name='date_search_vod_hoz'),
    path('predostavlenie-vodnyh-obektov/', ShowVodnieObject.as_view(), name='predostavlenie_vodnyh_obektov'),
    path('vodohozyajstvennye-meropriyatiya/', ShowVodHozMeropriyatiya.as_view(),
         name='vodohozyajstvennye_meropriyatiya'),
    path('monitoring-vodnyh-obektov/', ShowMonitoring.as_view(), name='monitoring_vodnyh_obektov'),
    path('bassejnovye-sovety/', ShowBassSovet.as_view(), name='bassejnovye_sovety'),
    path('ustanovlenie-rezhimov-vodohranilish/', ShowUstanovRezhim.as_view(), name='ustanovlenie_rezhimov'),
    path('skiovo-i-ndv/', ShowSkiovo.as_view(), name='skiovo_i_ndv'),
    path('kadrovoe-obespechenie/', ShowKadr.as_view(), name='kadrovoe_obespechenie'),
    path('svedeniya-o-predostavlenii-lgot/', ShowSvedeniyaOLgotah.as_view(), name='svedeniya_o_predostavlenii_lgot'),
    path('opredelenie-granic-zon-zatopleniya-podtopleniya/', ShowGraniciPodtop.as_view(),
         name='opredelenie_granic_zatopleniya'),
    path('likvidaciya-chs-v-irkutskoj-oblasti/', ShowChSIrk.as_view(), name='likvidaciya_chs')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
