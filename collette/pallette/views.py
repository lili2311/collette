from django.shortcuts import render, redirect
from collette.pallette.forms import ColourForm
from collette.pallette.models import Colour

# Create your views here.

def colour_list(request):
	if request.method == 'POST':
		form = ColourForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('pallette_colour_list')
	else:
		form = ColourForm()

	colours = Colour.objects.all()
	context = {'colours': colours, 'form': form}

	return render(request, 'pallette/colour_list.html', context)
