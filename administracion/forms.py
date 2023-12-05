# from datetime import datetime
import datetime

from django import forms
from ckeditor.fields import RichTextFormField

class Base_cliente(forms.Form):
    representante_legal=forms.CharField(max_length=50)
    razon_social=forms.CharField(max_length=80)
    doc_nit=forms.IntegerField(required=True)
    # descripcion=forms.CharField(max_length=300,widget=forms.Textarea)
    descripcion=RichTextFormField()
    num_inmuebles=forms.IntegerField()
    tipo_bien_raiz=forms.CharField(max_length=50)
    fecha_creacion=forms.DateField(initial=datetime.date.today())
    fecha_actualizacion=forms.DateField(initial=datetime.date.today())
    foto = forms.ImageField(required=False)
    
class Crear_cliente(Base_cliente):
    ...
        
class Buscar_Registro(forms.Form):
    razon_social=forms.CharField()
    
class Editar_Cliente(Base_cliente):
    fecha_actualizacion=forms.DateField()