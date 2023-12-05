from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from accounts.models import DatosExtra

from accounts.forms import Mi_formulario_sign_up, Editar_perfil

# Create your views here.
def login(request):
    formulario=AuthenticationForm()
    if request.method =='POST':
        formulario=AuthenticationForm(request,data=request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data.get('username')
            contraseña=formulario.cleaned_data.get('password')
            user = authenticate(username=usuario,password=contraseña)
            django_login(request,user)
            DatosExtra.objects.get_or_create(user=request.user)
            return redirect('inicio')
    return render(request,'accounts/login.html',{'form':formulario})


def signup(request):
    formulario= Mi_formulario_sign_up()
    
    if request.method == 'POST':
        formulario= Mi_formulario_sign_up(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    
    return render(request,'accounts/signup.html',{'form':formulario})


def perfil(request):
    return render(request,'accounts/perfil_usuario.html',{})

def update(request):
    datos_extra=request.user.datosextra

    formulario = Editar_perfil(instance=request.user,initial={'biografia': datos_extra.biografia,'avatar':datos_extra.avatar})
    if request.method=='POST':
        print('REQUEST.post ',request.POST)
        print('REQUEST.FILES ',request.FILES)
        formulario=Editar_perfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            nueva_biografia=formulario.cleaned_data.get('biografia')
            nuevo_avatar=formulario.cleaned_data.get('avatar')
            
            if nueva_biografia:
                datos_extra.biografia=nueva_biografia
            if nuevo_avatar:
                datos_extra.avatar=nuevo_avatar

            datos_extra.save()
            formulario.save()
            
            return redirect('/accounts/perfil')
    return render(request,'accounts/editar_perfil.html',{'form':formulario})

class CamnbioPassword(PasswordChangeView):
    template_name='accounts/cambiar_password.html'
    success_url=reverse_lazy('perfil')