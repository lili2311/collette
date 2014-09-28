from django.conf.urls import patterns, include, url
from collette.pallette.api_views import ColourListAPI


urlpatterns = patterns('',
    url(r'^colours/$', ColourListAPI.as_view(), name="api_pallette_colour_list"),
)
