from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

# Create your models here.
class Colour(models.Model):
	hex = models.CharField(max_length=6, unique=True,
		validators=[
	        RegexValidator(
	            regex='([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
	            message='Not a valid HEX colour',
	            code=None),
	        MinLengthValidator(3),
	        MaxLengthValidator(6),
	        ],
        )

	def __unicode__ (self):
		return self.hex


