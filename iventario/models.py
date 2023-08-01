from django.db import models

# Create your models here.
"""                  
en esta parte crearemos  nuestros molds ( nuestras tablas)

productos:
_id
_nombre
_precio
_stock
para crear un model , lo haremos del mismo modo que creamos una clase.
cada model , sera una calse que heredadd propiedsdes de la clase moldls
"""
class productos( models.Model):
    nombre = models.CharField(max_length=30, null=False)
    precio =models.FloatField()
    stock = models.IntegerField(default=0)
    
    


