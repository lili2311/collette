from django.db import models

# Create your models here.
class Colour(models.Model):
	hex = models.CharField(max_length=6, unique=True)

	def __unicode__ (self):
		return self.hex
