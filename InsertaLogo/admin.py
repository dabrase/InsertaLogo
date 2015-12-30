from django.contrib import admin

# Register your models here.
from .forms import RegistroForm
from .models import Registro

class RegistroAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "fecha_registro", "actualizado"]
	#class Meta:
	#	model = Registro
	form = RegistroForm

admin.site.register(Registro, RegistroAdmin)
