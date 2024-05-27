from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

# Vista para la página principal de la tienda
def tiendaPelicula(request):
    titulo = models.Titulo.objects.first()
    productos = models.Producto.objects.all()
    datos = {
        'titulo': titulo,
        'producto': productos,
    }
    return render(request, '2-quiz-index.html', datos)

# Vista para la página de detalles del producto
def ver_mas(request, producto_id):
    producto = get_object_or_404(models.Producto, id=producto_id)
    return render(request, '3-ver-mas.html', {'producto': producto})
