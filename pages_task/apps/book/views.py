# Create your views here.
from django.views.generic import ListView, CreateView, View
from models import *
from forms import AddNoteForm
from django.http import HttpResponse

class NotesList(ListView):
	"""
	This class render TextNotes list
	"""

	model = TextNote
	context_object_name = 'notes'
	template_name = 'index.html'


class AddNote(CreateView):
	"""
	This class provides ability	to create new
	instance of TextNote.
	If creation is successfully - redirect to
	list of notes
	"""
	model = TextNote
	form_class = AddNoteForm
	success_url = '/book/'

class PortableWidget(View):
	"""
	This class get random instance of TextNote
	from db and returns some formated html for
	widget render
	"""
	model = TextNote

	def get(self,request):
		"""
		This function get random record
		"""
		try:
			object = self.model.objects.order_by('?')[0]
		except IndexError:
			return HttpResponse('No records yet')

		return HttpResponse('''<div class = 'well'
		  style='width:300px;height:200px;padding:auto;'>
		  <b>Random Note</b>  : <p>{}</p> <p>{}</p>
		  		  </div>'''
		.format(object.name, object.value))
