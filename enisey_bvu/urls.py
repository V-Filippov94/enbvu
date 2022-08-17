from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'enisey_bvu'

urlpatterns = [
    path('funkcii-i-polnomochiya-enisejskogo-bvu/', ShowPage.as_view(), name='funkcii_i_polnomochiya'),
    path('normativnye_akty_function/', ShowPageNormativAkt.as_view(), name='normativnye_akty_function'),
    path('struktura-upravleniya/', ShowPageStructure.as_view(), name='struktura_upravleniya'),
    path('kontaktnye-dannye/', ShowPageContact.as_view(), name='kontaktnye_dannye'),
    path('podvedomstvennye-uchrezhdeniya/', ShowPageUchrezhdeniya.as_view(), name='podvedomstvennye_uchrezhdeniya'),
    path('perechni-informacionnyh-sistem-bankov-dannyh-reestrov-registrov/', ShowPagePerechniRegistr.as_view(),
         name='perechni_informacionnyh_sistem'),
    path('informaciya-ob-osushestvlenii-zakupok/', ShowPageInfoZakup.as_view(), name='info_zakupki'),
    path('plan-proverok-rezultaty-proverok/', ShowPagePlanProverok.as_view(), name='plan_proverok'),
    path('oficialnye-vystupleniya-i-zayavleniya/', ShowPageOficialVistup.as_view(), name='oficialnye_vystupleniya'),
    path('svedeniya-o-finansirovanii/', ShowPageInfoFinance.as_view(), name='svedeniya_o_finansirovanii')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
