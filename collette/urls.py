from django.conf.urls import include, url
from django.contrib import admin

from collette.pallette.views import colour_list, pallette_add

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('collette.api.urls')),
    url(r'^$', colour_list, name="pallette_colour_list"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^palette/add', pallette_add, name="pallette_add"),
]

