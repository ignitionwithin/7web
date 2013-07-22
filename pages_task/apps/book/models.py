from django.db import models
from django.contrib import admin
# Create your models here.
class TextNote(models.Model):
	note_name=models.CharField(max_length=20)
	note_value=models.CharField(max_length=500)

	def __unicode__(self):
		return self.note_name


admin.site.register(TextNote)