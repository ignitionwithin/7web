from django.db import models
from django.contrib import admin

# from django.core.validators import RegexValidator
# Create your models here.
class TextNote(models.Model):
	note_name  = models.CharField(max_length=20)
	note_value = models.CharField(max_length=500)
	note_image = models.ImageField(blank=True,upload_to='.')
	def __unicode__(self):
		return self.note_name


admin.site.register(TextNote)