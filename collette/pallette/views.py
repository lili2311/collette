from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from collette.pallette.forms import ColourForm, PalleteForm
from collette.pallette.models import Colour, Pallette


def colour_list(request):
	# if request.method == 'POST':
	# 	form = ColourForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('pallette_colour_list')
	# else:
	# 	form = ColourForm()

	colours = Colour.objects.all()
	context = {'colours': colours}


	return render(request, 'pallette/colour_list.html', context)

@login_required 
def pallette_add(request):
	if request.method == 'POST':
		form = PalleteForm(request.POST)
		if form.is_valid():
			pallette = form.save(commit=False)
			pallette.user = request.user
			pallette.save()
			return redirect('pallette_colour_list')
	else:
		form = PalleteForm()

	context = {'form': form}


	return render(request, 'pallette/pallette_add.html', context)
