"""insertaLogo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

#from django.conf.urls import patterns, include, url
#from django.conf.urls import include, url
#from django.contrib import admin
#from django.conf import settings

#admin.autodiscover()

#urlpatterns = patterns('',
#	url(r'^$','appInsertaLogo.views.inicio'),
#    url(r'^usuarios/$','appInsertaLogo.views.usuarios'),
#    url(r'^sobre/$','appInsertaLogo.views.sobre'),
#    url(r'^logos/$','appInsertaLogo.views.lista_logos'),
#    url(r'^logo/(?P<id_logo>\d+)$','appInsertaLogo.views.detalle_logo'),
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^media/(?P<path>.*)$','django.views.static.serve',
#		{'document_root':settings.MEDIA_ROOT,}
#	),
#    url(r'^contacto/$','appInsertaLogo.views.contacto'),
#    url(r'^receta/nueva/$','appInsertaLogo.views.nuevo_logo'),
#    url(r'^comenta/$','appInsertaLogo.views.nuevo_comentario'),
#    url(r'^usuario/nuevo$','appInsertaLogo.views.nuevo_usuario'),
#    url(r'^ingresar/$','appInsertaLogo.views.ingresar'),
#    url(r'^privado/$','appInsertaLogo.views.privado'),
#    url(r'^cerrar/$', 'appInsertaLogo.views.cerrar'),
#)
