from django.urls import path
from administracion.views import inicio,clientes,busqueda,detalle,borrar,editar


urlpatterns = [
    path('', inicio),
    path('clientes/',clientes),
    path('detalle/<int:cliente_id>',detalle, name='detalle_cliente'),
    path('detalle/<int:cliente_id>/borrar',borrar , name='borrar_cliente'),
    path('detalle/<int:cliente_id>/editar',editar, name='editar_cliente'),
    path('buscar/',busqueda)
]
