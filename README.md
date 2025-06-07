CODIGO FUENTE DE urls.py
from django.urls import path
from . import views
urlpatterns= [path('',views.saludo),

    path('saludo/<str:nombre>/', views.saludar_usuario),
    
 
    path('numero/<int:numero>/', views.mostrar_numero),
    ]



CODIGO FUENTE DE views.py:
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def saludo(request):
    return HttpResponse("Hola bro, bienvenido")

def saludar_usuario(request, nombre):
    return HttpResponse(f"hola {nombre} :)")

def mostrar_numero(request, numero):
    return HttpResponse(f"El número es el siguiente: {numero} :p")


EXPLICACIÓN:
Cada entrada de urlpatterns se encarga de ejecutar una funcion de views.py segun el URL que visite el usuario, despues de que el usuario visita alguna URL de las que estan definidas en las funciones estas reciben una peticion HTTP y devuelve una respuesta(segun la funcion que se ejecute).