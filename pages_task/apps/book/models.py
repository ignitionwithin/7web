from django.db import models
# Create your models here.
class TextNote(models.Model):
	""" This class describes Textnote required fields
	"""
	name  = models.CharField(max_length=20)
	value = models.CharField(max_length=500)
	image = models.ImageField(blank=True,upload_to='.')
	book  = models.ManyToManyField('Book', blank = True, null = True)
	def __unicode__(self):
		"""
		this function set represent name for this db record
		"""
		return self.name

class Book(models.Model):
	"""
	This class describes Book required fields
	"""
	name = models.CharField(max_length=20)
	def __unicode__(self):
		"""
		this function set represent name for this db record
		"""
		return self.name