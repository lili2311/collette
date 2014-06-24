from django.contrib import admin
from collette.pallette.models import Colour

# Register your models here.

class ColourAdmin(admin.ModelAdmin):
	search_fields = ("hex",)


admin.site.register(Colour, ColourAdmin)