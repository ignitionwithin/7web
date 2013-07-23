from django.db import models
from django.contrib import admin
from django.core.validators import RegexValidator
# Create your models here.
class TextNote(models.Model):
	note_name=models.CharField(max_length=20)
	note_value=models.CharField( validators=[RegexValidator(regex='^.{10}$', message='minimum lenght 10 chars', code='nomatch')],max_length=500)

	def __unicode__(self):
		return self.note_name


admin.site.register(TextNote)