# Create your views here.
from django.views.generic import ListView, CreateView, View
from models import *
from forms import AddNoteForm
from django.http import HttpResponse

class NotesList(ListView):

	model = TextNote
	context_object_name = 'notes'
	template_name = 'index.html'


class AddNote(CreateView):

	model = TextNote
	form_class = AddNoteForm
	success_url = '/book/'

class PortableWidget(View):

	model = TextNote

	def get(self,request):

		try:
			object = self.model.objects.order_by('?')[0]
		except IndexError:
			return HttpResponse('No records yet')

		return HttpResponse('''<div class = 'well'
		  style='width:300px;height:200px;padding:auto;'>
		  <b>Random Note</b>  : <p>{}</p> <p>{}</p>
		  		  </div>'''
		.format(object.name, object.value))
