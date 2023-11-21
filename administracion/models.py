from django.db import models

# Create your models here.

class Cliente(models.Model):
    representante_legal=models.CharField(max_length=50)
    razon_social=models.CharField(max_length=80)
    doc_nit=models.IntegerField()
    descripcion=models.CharField(max_length=250)
    num_inmuebles=models.IntegerField()
    tipo_bien_raiz=models.CharField(max_length=50)
    fecha_creacion=models.DateField()
    fecha_actualizacion=models.DateField()
    
    def __str__(self):
        return f'{self.id} - {self.doc_nit} - {self.razon_social} - {self.tipo_bien_raiz} - {self.fecha_creacion}'
    