from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'enisey_bvu'

urlpatterns = [
    path('funkcii-i-polnomochiya-enisejskogo-bvu/', FunctionBVU.as_view(), name='function_bvu'),
    path('normativnye_akty_function/', NormativAktFunction.as_view(), name='normativ_akt_function'),
    path('struktura-upravleniya/', StrukturaUpravleniya.as_view(), name='struktura_upravleniya'),
    path('podvedomstvennye-uchrezhdeniya/', PodvedomUchrezhdeniya.as_view(), name='podvedomstvennye-uchrezhdeniya'),
    path('perechni-informacionnyh-sistem-baz-dannyh-reestrov-registrov/', PerechniInfoSistem.as_view(),
         name='perechni_info_sistem'),
    path('informaciya-ob-osushestvlenii-zakupok/', InfoZakupok.as_view(), name='info_zakupki'),
    path('plan-proverok-rezultaty-proverok/', PlanProverki.as_view(), name='plan_proverok'),
    path('oficialnye-vystupleniya-i-zayavleniya/', OficialVystupleniya.as_view(), name='oficialnye_vystupleniya'),
    path('svedeniya-o-finansirovani-sredstv-massovoj-informacii/', SvedeniyaOSmi.as_view(),
         name='svedeniya_o_finansirovanii')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
