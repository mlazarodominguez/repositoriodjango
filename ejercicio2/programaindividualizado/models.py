from django.db import models

# Create your models here.

class Residente(models.Model):
    nombre = models.TextField((""))
    apellidos = models.TextField((""))
    fecha_nacimiento = models.DateField((""), auto_now=False, auto_now_add=False)
class Familiar(models.Model):
    nombre = models.TextField((""))
    apellidos = models.TextField((""))
    fecha_nacimiento = models.DateField((""), auto_now=False, auto_now_add=False)
    parentesco= models.TextField((""))

class ParteInforme(models.Model):
    LOAN_STATUS = (
        ('S', 'SANITARIA'),
        ('F', 'FUNCIONAL'),
        ('P', 'PSIQUICA'),
        ('S', 'SOCIAL'),
        ('TO','TERAPIA OCUPACIONAL'),
    )

    tipo = models.CharField( max_length=2,choices=LOAN_STATUS)
    valoracion_inicial = models.IntegerField((""))
    objetivos = models.TextField((""))
    informe = models.ManyToManyField("Informe", verbose_name=(""))
class Informe(models.Model):
    fecha_informe = models.DateField((""), auto_now=False, auto_now_add=False)
    partes = models.ManyToManyField("ParteInforme",related_name="Partes", verbose_name=(""))
    
    
    
    
    
    
    
    
    
    
    
    
    
   