from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleado

def index(request):
  
  posts = Empleado.objects.all()
  for obj in posts:
    print(obj.nombre)
  return HttpResponse("Nombre del empleado)")

def storage(resquest, nombre,apellido,cargo,funcion,rol):
  
  #creamos la isntancia
  post = Empleado (nombre = nombre, apellido = apellido, cargo = cargo, funcion= funcion, rol = rol)
  post.save()
  #trabajar con el modelo
  return HttpResponse("guardamos en el modelo, ")


#metodo para buscar por id
def consultar (resquest,id):
  post = Empleado.objects.get (id=id)
  return HttpResponse (f"Nombre:{post.nombre}, Apellido: {post.apellido}, Cargo:{post.cargo}, Funcion: {post.funcion}, rol: {post.rol} ")