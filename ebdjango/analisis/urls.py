from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from analisis.views import *
urlpatterns = [
    path('limpiar_novedades/', limpiar_novedades, name="limpiarnov"),
    path('limpiar_acta/', limpiar_acta, name="limpiaracta"),
    path('calculo_novedades/', calculo_novedades_acta, name="calculo_novedades"),
    path('novedades-acta/', novedades_acta, name="novedades_acta"),
       
]