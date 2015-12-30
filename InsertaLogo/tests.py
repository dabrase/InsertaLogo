from django.test import TestCase

# Create your tests here.
from django import forms
from .models import Registro
from .forms import RegistroForm

class TestRunninU(TestCase):
	def test_registros(self):
		reg = Registro(email = 'email', nombre = 'nombre',apellidos = 'apellidos')
		reg.save()
		self.assertEqual(reg.nombre,'nombre')
		print("Se ha creado usuario, Test = OK")

	def test_cambiar_nombre(self):
		reg = Registro(email = 'email', nombre = 'nombre',apellidos = 'apellidos')
		reg.save()
		reg.nombre='CambioNombre'
		reg.save()
		self.assertEqual(reg.nombre,'CambioNombre')
		print("Se ha realizado el cambio de nombre, Test = OK")


	def test_cambiar_email(self):
		reg = Registro(email = 'email', nombre = 'nombre',apellidos = 'apellidos')
		reg.save()
		reg.email='CambioEmail'
		reg.save()
		self.assertEqual(reg.email,'CambioEmail')
		print("Se ha realizado el cambio de email, Test = OK")
