from django.urls import path
from administracion.views import inicio,clientes,busqueda,detalle,borrar,editar,about


urlpatterns = [
    path('', inicio, name='inicio'),
    path('clientes/',clientes),
    path('clientes/<int:cliente_id>',detalle, name='detalle_cliente'),
    path('clientes/<int:cliente_id>/borrar',borrar , name='borrar_cliente'),
    path('clientes/<int:cliente_id>/editar',editar, name='editar_cliente'),
    path('buscar/',busqueda),
    path('about_me/',about)
]
