from django.db import models
# Create your models here.
class TextNote(models.Model):
	note_name  = models.CharField(max_length=20)
	note_value = models.CharField(max_length=500)
	note_image = models.ImageField(blank=True,upload_to='.')
	note_book  = models.ManyToManyField('Book', blank = True, null = True)
	def __unicode__(self):
		return self.note_name

class Book(models.Model):
	book_name = models.CharField(max_length=20)
	def __unicode__(self):
		return self.book_name