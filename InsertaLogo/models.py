from django.db import models

# Create your models here.
class Registro(models.Model):
	email = models.EmailField()
	nombre = models.CharField(blank=True, null=True, max_length = 25)
	apellidos = models.CharField(blank=True, null=True, max_length = 50)
	fecha_registro = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): 
		return self.nombre
