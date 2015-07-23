from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import IndexView

urlpatterns = patterns('',
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', IndexView.as_view(), name='home'),
    url(r'^', include('clinic.urls', namespace='clinic')),
)
