from django.db import models

# Create your models here.
class Modelo(models.Model):
  nombre=models.CharField(max_length=50)
  apellido=models.CharField(max_length=50)
  edad=models.IntegerField()
  cadena=models.CharField(max_length=200)
  fecha=models.DateField(auto_now_add=True)