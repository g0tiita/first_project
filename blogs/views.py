from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
#def index(request):
#    respuesta = "Holiiiii a todos!! (:"
#    return HttpResponse(respuesta)

#otra vista
#def adios(request):
#    respuesta = "Chao pescao"
#    return HttpResponse(respuesta)

def root(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

# edirige a la ruta "/" y se debe importar redirect
def create(request):
    return redirect("/") 

def show(request, number):
    return HttpResponse(f"placeholder para mostrar el blog numero: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder para mostrar el blog numero: {number}")

def destroy(request, number):
    return redirect("/blogs")

def profile(request):
    data = {
        'name': 'Macarena',
        'location': 'Temuco'
    }
    return JsonResponse(data)

