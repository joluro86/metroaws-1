from django.urls import path
from programacion.views import *

urlpatterns = [
    path('acrev/', acrev, name="acrev"),
    path('amrtr/', amrtr, name="amrtr"),
    path('legalizaciones/', lega, name="lega"),
    path('inconsistencias/', inconsistencias, name="inconsistencias"),
    path('programador/', programador, name="programador"),
] 