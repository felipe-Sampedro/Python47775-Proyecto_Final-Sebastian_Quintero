from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class Mi_formulario_sign_up(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contrasenia", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={'username':'','email':'','password1':'','password2':''}
        
        
class Editar_perfil(UserChangeForm):
    password = None
    email = forms.EmailField(label='Cambiar email', required=False)
    # first_name = forms.CharField(label='Cambiar nombre', required=False)
    # last_name = forms.CharField(label='Cambiar apellido', required=False)
    # biografia = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    # avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['username','email']
        help_texts={'username':'','email':''}