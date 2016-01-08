from django.conf import settings
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'InsertaLogo.views.home', name='home'),
    url(r'^contacto/$', 'InsertaLogo.views.contacto', name='contacto'),
    url(r'^fluid/$', 'InsertaLogo.views.fluid', name='fluid'),
    url(r'^base/$', 'InsertaLogo.views.base', name='base'),
    url(r'^sobre/$', 'InsertaLogo.views.sobre', name='sobre'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
