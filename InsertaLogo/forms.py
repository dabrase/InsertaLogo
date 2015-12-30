from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
	class Meta:
		model = Registro
		fields = ['email', 'nombre','apellidos']
		# exclude = ['nombre']

	#Validaciones
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not domain == "gmail":
			raise forms.ValidationError("Debe utilizar una cuenta de Gmail")
		if not extension == "com":
			raise forms.ValidationError("Por favor, la extension debe ser .com")
		return email

	def clean_nombre(self):
		nombre = self.cleaned_data.get('nombre')
		#Escribir codigo de validacion
		return nombre

	def clean_apellidos(self):
		apellidos = self.cleaned_data.get('apellidos')
		#Escribir codigo de validacion
		return apellidos

class ContactoForm(forms.Form):
	email = forms.EmailField()
	nombre = forms.CharField(required=False,max_length = 25)
	mensaje = forms.CharField(max_length = 250)
	
	#Validaciones
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not domain == "gmail":
			raise forms.ValidationError("Debe utilizar una cuenta de Gmail")
		if not extension == "com":
			raise forms.ValidationError("Por favor, la extension debe ser .com")
		return email

		