# Create your views here.
from django.views.generic import ListView, CreateView, View
from models import *
from forms import AddNoteForm
from django.http import HttpResponse

class Notes_list(ListView):

	model = TextNote
	context_object_name = 'notes'
	template_name = 'index.html'


class Add_note(CreateView):

	model = TextNote
	form_class = AddNoteForm
	success_url = '/book/'

class Portable_widget(View):

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
		.format(object.note_name, object.note_value))
