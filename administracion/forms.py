
from django import forms


class Crear_cliente(forms.Form):
    representante_legal=forms.CharField(max_length=50)
    razon_social=forms.CharField(max_length=80)
    doc_nit=forms.IntegerField(required=True)
    descripcion=forms.CharField(max_length=250)
    num_inmuebles=forms.IntegerField()
    tipo_bien_raiz=forms.CharField(max_length=50)
    fecha_creacion=forms.DateField()
    fecha_actualizacion=forms.DateField()
    
    
class Buscar_Registro(forms.Form):
    razon_social=forms.CharField(max_length=80)