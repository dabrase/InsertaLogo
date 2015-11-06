

# Register your models here.

#from appInsertaLogo.models import Logo, Comentario
from django.contrib import admin
from .models import Usuario

admin.site.register(Usuario)

#admin.site.register(Logo)
#admin.site.register(Comentario)