#encoding:utf-8 
#from django.forms import ModelForm
from django import forms
#from appInsertaLogo.models import Logo, Comentario
from appInsertaLogo.models import Usuario

#class crea_usuario(object):
#	"""docstring for crea_usuario"""
#	def __init__(self, arg):
#		super(crea_usuario, self).__init__()
#		self.arg = arg
		
class crea_usuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre','apellidos','user','password', 'email')
		

#class ContactoForm(forms.Form):
#	correo = forms.EmailField(label = 'Tu correo electrónico')
#	mensaje = forms.CharField(widget = forms.Textarea)

#class LogoForm(ModelForm):
#    class Meta:
#        model = Logo

#class ComentarioForm(ModelForm):
#    class Meta:
#        model = Comentario
