from django.shortcuts import render, redirect
from administracion.forms import Crear_cliente,Buscar_Registro
from administracion.models import Cliente

# Create your views here.
def inicio(request):
    return render(request,'base.html',{})

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
    cliente_buscar=request.GET.get('Cliente')
    if cliente_buscar:
        lista_clientes=Cliente.objects.filter(razon_social__icontains=cliente_buscar)
    else:
        lista_clientes=Cliente.objects.all()
    
    formulario= Buscar_Registro()
    return render(request,'administracion/buscar.html',{'lista_clientes':lista_clientes,'formulario':formulario})