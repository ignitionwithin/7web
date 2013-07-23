# Create your views here.
from django.views.generic import ListView, CreateView
from models import *
from django.core.urlresolvers import reverse


class Notes_list(ListView):
	model = TextNote
	context_object_name = 'notes'
	template_name = 'index.html'


class Add_note(CreateView):
	model = TextNote
	success_url = '/book/'