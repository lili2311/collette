from django.conf.urls import include, url
from collette.pallette.api_views import ColourListAPI


urlpatterns = [
    url(r'^colours/$', ColourListAPI.as_view(), name="api_pallette_colour_list"),
]
