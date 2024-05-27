from django.db import models

# Create your models here.
class Titulo(models.Model):
    msj = models.CharField(max_length=200)
    def __str__(self):
        return self.msj

class Producto(models.Model):
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nombre + ' - ' + self.descripcion