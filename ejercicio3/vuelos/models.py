from django.db import models

# Create your models here.
class Aeropuerto(models.Model):
    nombre = models.TextField((""))
    ciudad= models.TextField((""))
    siglas = models.TextField((""))
class Vuelo(models.Model):
    aeropuerto_salida = models.ForeignKey("Aeropuerto", related_name="Aeropuertosalida",verbose_name=(""), on_delete=models.CASCADE)
    fecha_salida = models.DateField((""), auto_now=False, auto_now_add=False)
    aeropuerto_llegada = models.ForeignKey("Aeropuerto",related_name="Aeropuertollegada", verbose_name=(""), on_delete=models.CASCADE)
    fecha_llegada = models.DateField((""), auto_now=False, auto_now_add=False)
    codigo_vuelo = models.TextField((""))
class Cliente(models.Model):
    nombre = models.TextField((""))
    apellidos = models.TextField((""))
    email = models.EmailField((""), max_length=254)
    fecha_nacimiento = models.DateField((""), auto_now=False, auto_now_add=False)
class Reserva(models.Model):
    vuelo = models.ForeignKey("Vuelo", verbose_name=(""), on_delete=models.CASCADE)
    cliente = models.ForeignKey("Cliente", verbose_name=(""), on_delete=models.CASCADE)
    fecha_reserva = models.DateField((""), auto_now=False, auto_now_add=False)
    precio = models.FloatField((""))
    