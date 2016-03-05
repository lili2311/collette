from django.conf.urls import include, url
from django.contrib import admin

from collette.pallette.views import colour_list

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('collette.api.urls')),
    url(r'^$', colour_list, name="pallette_colour_list"),
]

