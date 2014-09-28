# built in imports
# 3rd party in imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# first party (mine) in imports
# from collette.pallette.serializers import ColourSerializer
from collette.pallette.models import Colour
from collette.pallette.api_forms import ColourListForm

class ColourListAPI(APIView):

	def get(self, request):
		colour_list_form = ColourListForm(request.GET)
		if not colour_list_form.is_valid():
			return Response(colour_list_form.errors, status=status.HTTP_400_BAD_REQUEST)

		limit = colour_list_form.cleaned_data.get('limit')
		colours = Colour.objects.all().values_list('hex', flat=True).order_by('?')
		# serializer = ColourSerializer(colours, many=True) 
		# not needed as we only want to return a colour list for now
		if limit:
			colours = colours[:limit]

		return Response(colours, status=status.HTTP_200_OK)



