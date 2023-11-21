from django.urls import path
from administracion.views import inicio,clientes,busqueda,detalle


urlpatterns = [
    path('', inicio),
    path('clientes/',clientes),
    path('detalle/<int:cliente_id>',detalle, name='detalle_cliente'),
    path('buscar/',busqueda)
]
