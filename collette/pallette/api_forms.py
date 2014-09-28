from django import forms

class ColourListForm(forms.Form):

	limit = forms.IntegerField(required=False)

