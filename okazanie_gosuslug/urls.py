from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'okazanie_gosuslug'

urlpatterns = [
    path('predostavlenie-svedenij-iz-gos-vod-reestra/', ShowSvedeniyaGosReestr.as_view(), name='svedeniya_vod_reestra'),
    path('predostavlenie-vodnyh-obektov-v-polzovanie/', ShowPolzovanieVodObject.as_view(),
         name='polzovanie_vod_object'),
    path('predostavlenie-v-polzovanie/', ShowPredostavVPolz.as_view(), name='predostavlenie_v_polzovanie'),
    path('utverzhdenie-normativov-dopustimyh-sbrosov/', ShowUtverzhdenieSbrosov.as_view(), name='utverzhdenie_sbrosov'),
    path('vydacha-razresheniya-na-sozdanie-iskusstvennogo-zemelnogo-uchastka/', ShowZemUchastok.as_view(),
         name='razresheniya_zemelnogo_uchastka')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
