from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'normativ_document'

urlpatterns = [
    path('normativ-akt-rosvodresursy/', NormAktRosvodres.as_view(), name='normativ_akt_rosvodresursy')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
