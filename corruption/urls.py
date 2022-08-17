from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = 'corruption'

urlpatterns = [
    path('akty-v-sfere-protivodejstviya-korrupcii/', ShowAktyAntiCorruption.as_view(), name='akty_anti_corruption'),
    path('antikorrupcionnaya-ekspertiza/', ShowAntiKorEkspertiza.as_view(), name='antikorrupcionnaya_ekspertiza'),
    path('metodicheskie-materialy/', ShowMetodiMaterial.as_view(), name='metodicheskie_materialy'),
    path('dokumenty-svyazanne-s-protivodejstviem-korrupcii/', ShowDocAntiCor.as_view(), name='doc_anti_cor'),
    path('svedeniya-o-dohodah/', ShowSvedeniyaODohodah.as_view(), name='svedeniya_o_dohodah'),
    path('komissiya-po-soblyudeniyu-trebovanij/', ShowKomissiya.as_view(), name='komissiya'),
    path('obratnaya-svyaz-dlya-soobshenij-o-faktah-korrupcii/', ShowLinkAntiCor.as_view(), name='obratnaya_svyaz'),
    path('doklady-otchety-obzory/', ShowDokladObzor.as_view(), name='doklady_otchety_obzory'),
    path('chasto-zadavaemye-voprosy/', ShowFAQ.as_view(), name='chasto_zadavaemye_voprosy')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)