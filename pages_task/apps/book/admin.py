from django.contrib import admin
from models import TextNote, Book
from forms import AddNoteForm


class TextNote_Admin(admin.ModelAdmin):
    """
    This class make model relation to the form
    """
    form = AddNoteForm

#  Register needed models to django admin
admin.site.register(TextNote, TextNote_Admin)
admin.site.register(Book)
