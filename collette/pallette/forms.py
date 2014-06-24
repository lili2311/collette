from django import forms
from collette.pallette.models import Colour 

class ColourForm(forms.ModelForm):

	class Meta:
		model = Colour
		fields = ('hex',) 
