from django.urls import path
from administracion.views import inicio,clientes,busqueda

urlpatterns = [
    path('', inicio),
    path('clientes/',clientes),
    path('buscar/',busqueda)
]
