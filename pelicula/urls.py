from django.urls import path
from . import views

urlpatterns = [
    path('', views.tiendaPelicula, name='index'),
    path('ver-mas/<int:producto_id>/', views.ver_mas, name='ver_mas'),
]
