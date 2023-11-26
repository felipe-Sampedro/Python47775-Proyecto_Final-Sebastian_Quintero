import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from administracion.forms import Crear_cliente,Buscar_Registro,Editar_Cliente
from administracion.models import Cliente

# Create your views here.
def inicio(request):
    return render(request,'administracion/inicio.html',{})

@login_required
def clientes(request):
    if request.method=='POST':
        formulario=Crear_cliente(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            representante_legal=info_limpia.get('representante_legal')
            razon_social=info_limpia.get('razon_social')
            doc_nit=info_limpia.get('doc_nit')
            descripcion=info_limpia.get('descripcion')
            num_inmuebles=info_limpia.get('num_inmuebles')
            tipo_bien_raiz=info_limpia.get('tipo_bien_raiz')
            fecha_creacion=info_limpia.get('fecha_creacion')
            fecha_actualizacion=info_limpia.get('fecha_actualizacion')
            
            registro = Cliente(
                representante_legal=representante_legal,
                razon_social=razon_social.lower(),
                doc_nit=doc_nit,
                descripcion=descripcion,
                num_inmuebles=num_inmuebles,
                tipo_bien_raiz=tipo_bien_raiz,
                fecha_creacion=fecha_creacion,
                fecha_actualizacion=fecha_actualizacion
                )
            
            registro.save()
            return redirect('/buscar')
        else:
            return render(request,'administracion/crear_cliente.html',{'formulario':formulario})
            
    formulario=Crear_cliente()
    return render(request,'administracion/crear_cliente.html',{'formulario':formulario})


def busqueda(request):
    cliente_buscar=request.GET.get('razon_social')
    print(cliente_buscar)
    if cliente_buscar:
        lista_clientes=Cliente.objects.filter(razon_social__icontains=cliente_buscar)
    else:
        lista_clientes=Cliente.objects.all()
    
    formulario= Buscar_Registro()
    return render(request,'administracion/buscar.html',{'lista_clientes':lista_clientes,'formulario':formulario})


def detalle(request,cliente_id):
    cliente=Cliente.objects.get(id=cliente_id)
    return render(request,'administracion/detalle_cliente.html',{'cliente':cliente})

@login_required
def borrar(request,cliente_id):
    cliente_borrar=Cliente.objects.get(id=cliente_id)
    cliente_borrar.delete()
    return redirect('/buscar')

@login_required
def editar(request,cliente_id):
    cliente_editar=Cliente.objects.get(id=cliente_id)
    if request.method =='POST':
        formulario=Editar_Cliente(request.POST)
        if formulario.is_valid():
            info_nueva=formulario.cleaned_data
            cliente_editar.representante_legal=info_nueva.get('representante_legal')     
            cliente_editar.razon_social=info_nueva.get('razon_social')     
            cliente_editar.doc_nit=info_nueva.get('doc_nit')     
            cliente_editar.descripcion=info_nueva.get('descripcion')     
            cliente_editar.num_inmuebles=info_nueva.get('num_inmuebles')     
            cliente_editar.tipo_bien_raiz=info_nueva.get('tipo_bien_raiz')     
            cliente_editar.fecha_creacion=info_nueva.get('fecha_creacion')     
            cliente_editar.fecha_actualizacion=info_nueva.get('fecha_actualizacion')     
            cliente_editar.save()
            return redirect('/buscar')  
        else:
            return render(request,'administracion/editar_cliente.html',{'formulario':formulario})  
               
    formulario = Editar_Cliente(initial={
        'representante_legal':cliente_editar.representante_legal,
        'razon_social':cliente_editar.razon_social,
        'doc_nit':cliente_editar.doc_nit,
        'descripcion':cliente_editar.descripcion,
        'num_inmuebles':cliente_editar.num_inmuebles,
        'tipo_bien_raiz':cliente_editar.tipo_bien_raiz,
        'fecha_creacion':cliente_editar.fecha_creacion,
        'fecha_actualizacion':datetime.date.today,
        })
    return render(request,'administracion/editar_cliente.html',{'formulario':formulario})


def about(request):
    return render(request,'administracion/about_me.html',{})