from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.forms import Mi_formulario_sign_up


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