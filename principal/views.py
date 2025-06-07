from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def saludo(request):
    return HttpResponse("Hola bro, bienvenido")

def saludar_usuario(request, nombre):
    return HttpResponse(f"hola {nombre} :)")

def mostrar_numero(request, numero):
    return HttpResponse(f"El número es el siguiente: {numero} :p")