from django.db import models
#from django.contrib.auth.models import User

class Usuario(models.Model):
	nombre = models.CharField(max_length = 50)
	apellidos = models.CharField(max_length = 80)
	user = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)
	email = models.TextField(verbose_name='Email', help_text='Direccion de correo Electronico') 

	def __str__(self):
		return self.nombre

class Admin:
    pass

# Create your models here.
#class Logo(models.Model):

#	nombre = models.CharField(max_length=100)
#	email = models.TextField(verbose_name='Email', help_text='Direccion de correo Electronico')
#	imagenLogo = models.ImageField(upload_to='logos', verbose_name='Imagen')
#	usuario = models.ForeignKey(User)

#	def __str__(self):
#		return self.nombre

#class Comentario(models.Model):
#    logo = models.ForeignKey(Logo)
#    texto = models.TextField(help_text = 'Tu comentario', verbose_name='Comentario')

#    def __unicode__(self):
#        return self.texto
