from django import forms
from collette.pallette.models import Colour, Pallette

class ColourForm(forms.ModelForm):

	class Meta:
		model = Colour
		fields = ('hex',) 		 

class PalleteForm(forms.ModelForm):

	class Meta:
		model = Pallette
		fields = ('name',) 		 
