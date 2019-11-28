from django.db import models


class Categoria(models.Model):
    nombre = models.TextField((""))
    categoria_padre = models.ForeignKey("Categoria", verbose_name=(""), on_delete=models.CASCADE)
    
class Producto(models.Model):

    nombre = models.TextField((""))
    descripcion = models.TextField((""))
    url_image = models.TextField((""))
    precio_unidad = models.IntegerField((""))
    categoria = models.ForeignKey("Categoria", verbose_name=(""), on_delete=models.CASCADE)