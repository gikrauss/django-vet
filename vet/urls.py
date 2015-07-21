from django.conf.urls import patterns, include, url
from django.contrib import admin
from vet.views import IndexView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', IndexView.as_view()),
)
