from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'appeal'

urlpatterns = [
    path('obrashenie-k-rukovoditelyu/', AppealHeadFormView.as_view(), name='appeal_head'),
    path('informaciya-o-rabote-s-obrasheniyami-grazhdan/', ShowInfoObrasheniya.as_view(),
         name='informaciya_o_rabote_s_grazhdanami')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
