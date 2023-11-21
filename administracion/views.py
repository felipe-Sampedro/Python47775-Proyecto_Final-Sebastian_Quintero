from django.shortcuts import render
from administracion.forms import Crear_cliente,Buscar_Registro

# Create your views here.
def inicio(request):
    return render(request,'base.html',{})

def clientes(request):
    formulario=Crear_cliente()
    return render(request,'administracion/crear_cliente.html',{'formulario':formulario})

def busqueda(request):
    formulario= Buscar_Registro()
    lista_clientes=[]
    return render(request,'administracion/buscar.html',{'lista_clientes':lista_clientes,'formulario':formulario})