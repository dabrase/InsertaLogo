#from django.test import TestCase

# Create your tests here.

#class SimpleTest(TestCase):
#    def test_basic_addition(self):
#        """
#        Tests that 1 + 1 always equals 2.
#        """
#        self.assertEqual(1 + 1, 2)

from django.test import TestCase
from django import forms

from .models import Usuario
from .forms import crea_usuario

class TestRunninU(TestCase):
	def test_usuarios(self):
		user = Usuario(nombre = 'nombre',apellidos = 'apellidos',user = 'user',password = 'pass', email = 'email')
		user.save()
		self.assertEqual(user.nombre,'nombre')
		print("Se ha creado usuario, Test = OK")

	def test_cambiar_nombre(self):
		user = Usuario(nombre = 'nombre',apellidos = 'apellidos',user = 'user',password = 'pass', email = 'email')
		user.save()
		user.nombre='CambioNombre'
		user.save()
		self.assertEqual(user.nombre,'CambioNombre')
		print("Se ha realizado el cambio de nombre, Test = OK")


	def test_cambiar_email(self):
		user = Usuario(nombre = 'nombre',apellidos = 'apellidos',user = 'user',password = 'pass', email = 'email')
		user.save()
		user.email='CambioEmail'
		user.save()
		self.assertEqual(user.email,'CambioEmail')
		print("Se ha realizado el cambio de email, Test = OK")

class TestRunninFU(TestCase):
	def test_form_usuarios(self):
		data_form = {'nombre' : 'nombre','apellidos' : 'apellidos','user' : 'user', 'password': 'pass', 'email':'email'}
		form = crea_usuario(data = data_form)
		self.assertTrue(form.is_valid())
		print("Formulario Usuario, Test = OK")