from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = 'kadr_provision'

urlpatterns = [
    path('poryadok-postupleniya-na-sluzhbu/', ShowPorydokpostupleniya.as_view(), name='poryadok_postupleniya'),
    path('svedeniya-o-vakantnih-dolzhnostyah/', ShowSvedeniyaVakansii.as_view(), name='svedeniya_o_dolzhnostyah'),
    path('result-konkurs/', ShowResultKonkurs.as_view(), name='result_konkurs'),
    path('kontakty-po-voprosu-zamesheniya/', ShowContactPoVakansiyam.as_view(), name='kontakty_po_voprosu_zamesheniya'),
    path('sostav-komissii/', ShowSostavKomissii.as_view(), name='sostav-komissii'),
    path('obzhalovanie-result/', ShowObzhalovanieResult.as_view(), name='obzhalovanie_result')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)