from django.contrib import admin
from django.urls import path
from gestionvencimientos.views import *
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls, name="administrador"),
    path('', index, name="home"),
     path('pendientes/<int:id_dia>', calculo_pendientes, name="pendientes"),
    path('proxsemana/<int:id_dia>', calculo_next_week, name="pendientes_next_week"),
    path('antsemana/<int:id_dia>', calculo_last_week, name="pendientes_last_week"),
    path('pendientes/', menu_pendientes, name="menu_pendientes"),
    path('limpiar/', limpiar_base, name="limpiar"),
    path('eliminar/', eliminar_bd, name="eliminar"),
    path('fechas/', fechas, name="fechas"),
    path('vencidos/', vencidos, name="vencidos"),
    path('vencidos_todos/', busqueda_vencidos, name="vencidos_todos"),
    path('gestion/', gestion_bd, name="gestionbd"),
    path('cerrar/<int:id_pedido>/', cerrar_pedido, name="cerrar"),
    path('week/<int:id_week>/', pedidos_week, name="week"),
    path('otros/<int:cliente>/<int:apla>/<int:pendi>/', otros_pedidos, name="otros"),
    path('epm/<str:inicio>/<str:final>/', vencimientos_epm, name="epm"),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('comparativo/', include('perseovsfenix.urls')),
    path('analisis/', include('analisis.urls')),
    path('programar/', include('programacion.urls')),
]