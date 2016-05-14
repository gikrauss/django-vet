from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import IndexView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^clinica/', include('clinic.urls', namespace='clinic')),
    url(r'^finanzas/', include('finances.urls', namespace='finances')),
    url(r'^settings/', include('settings.urls', namespace='settings')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
