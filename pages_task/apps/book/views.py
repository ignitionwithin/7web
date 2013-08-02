# Create your views here.
from django.views.generic import ListView, CreateView
from models import *
from django.core.urlresolvers import reverse_lazy
from forms import AddNoteForm

class Notes_list(ListView):
	model = TextNote
	context_object_name = 'notes'
	template_name = 'index.html'


class Add_note(CreateView):
	model = TextNote
	form_class = AddNoteForm
	success_url = '/book/'