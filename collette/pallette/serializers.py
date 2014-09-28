from rest_framework import serializers
from collette.pallette.models import Colour

class ColourSerializer(serializers.ModelSerializer):

	class Meta:
		model = Colour
		fields = ('hex',)