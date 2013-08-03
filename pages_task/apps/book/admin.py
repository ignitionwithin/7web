from django.contrib import admin
from models import TextNote, Book
from forms import AddNoteForm

class TextNote_Admin(admin.ModelAdmin):


	form = AddNoteForm


admin.site.register(TextNote, TextNote_Admin)
admin.site.register(Book)