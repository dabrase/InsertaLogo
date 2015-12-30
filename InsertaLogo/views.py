from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import RegistroForm, ContactoForm

# Create your views here.
def base(request):
	return render(request, "base.html")

def home(request):
	titulo = 'Bienvenido'

	#Declaracion form
	form =  RegistroForm(request.POST or None)

	contexto = {
		"template_title": titulo,
		"a": 123,
		"form": form
	}

	if form.is_valid():
		instancia = form.save(commit=False)
		
		nombre = form.cleaned_data.get("nombre")
		if not nombre:
			nombre = "Nuevo nombre"
		instancia.nombre = nombre

		instancia.save()
		contexto = {
			"template_title": "Gracias"
		}


	'''
	if form.is_valid():
		form.save()

	contexto = {
		"template_title": "Gracias"
	}
	'''

	'''
	if request.user.is_authenticated():
		titulo = "Inserta Logo %s" %(request.user)
	'''

	'''
	#Aniade una form
	print request
	if request.method == "POST":
		print request.POST
	'''

	'''
	if form.is_valid():
		instancia = form.save(commit=False)
		if not instancia.nombre:
			instancia.nombre = "Magv"
		instancia.save()
		print instancia.email
		print instancia.nombre
		print instancia.fecha_registro
		
		contexto = {
			"template_title": "Gracias"
		}
	'''

	return render(request, "home.html",contexto)


def contacto(request):
	form = ContactoForm(request.POST or None)
	if form.is_valid():
		#for i, value in form.cleaned_data.iteritems():
		#	print i, value
			#print form.cleaned_data.get(i)

		form_email = form.cleaned_data.get("email")
		form_nombre = form.cleaned_data.get("nombre")
		form_mensaje = form.cleaned_data.get("mensaje")
		#print email, nombre, mensaje

		subject = 'Formulario de contacto del sitio'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'otroEmail@gmail.com']
		contact_message = "%s: %s via %s"%(
			form_nombre, 
			form_mensaje, 
			form_email)
		some_html_message = """
		<h1> Hola </h1>
		"""

		send_mail(subject, 
			contact_message, 
			from_email, 
			to_email,
			html_message=some_html_message,
			fail_silently=True)
	
	contexto = {
		"form": form,
	}
	return render(request, "contacto.html",contexto)