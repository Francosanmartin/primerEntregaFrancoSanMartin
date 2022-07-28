from datetime import datetime
from django.shortcuts import render
from desafio.models import Modelo
from datetime import datetime
# Create your views here.

def persona(request):
  datos=Modelo.objects.create(nombre="Pedro",apellido="Lopez",edad=24,cadena="tercera persona creada",fecha=datetime.now())
  context={
    'datos':datos
  }
  return render(request,'familiar.html',context=context)

def baseDatos(request):
  todos=Modelo.objects.all()
  context={
    'todos':todos
  }
  return render(request,'familiares.html',context=context)