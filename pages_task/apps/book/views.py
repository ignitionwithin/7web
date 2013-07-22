# Create your views here.
from django.views.generic import ListView
from models import *

class Notes_list(ListView):
	model = TextNote
	context_object_name = 'notes'
	template_name = 'index.html'