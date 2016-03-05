from django.contrib import admin
from collette.pallette.models import Colour, Pallette

# Register your models here.

class ColourAdmin(admin.ModelAdmin):
	search_fields = ("hex",)

class PalletteAdmin(admin.ModelAdmin):
	search_fields = ("name",)

admin.site.register(Colour, ColourAdmin)
admin.site.register(Pallette, PalletteAdmin)