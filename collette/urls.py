from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('collette.api.urls')),
    url(r'^$', 'collette.pallette.views.colour_list', name="pallette_colour_list"),
)
