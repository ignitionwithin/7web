# Create your views here.
from django.views.generic import ListView, CreateView, View
from models import *
from forms import AddNoteForm
import json
from django.http import HttpResponse
import random

# class AjaxMixin(object):
#
# 	def render_to_json_response(self,context, **response_kwargs):
# 		data = json.dumps(context)
# 		response_kwargs['content_type'] = 'application/json'
# 		return HttpResponse(data, **response_kwargs)
#
# 	def form_invalid(self,form):
# 		response = super(AjaxMixin,self).form_invalid(form)
# 		if self.request.is_ajax():
# 			return self.render_to_json_response(form.errors, status= 400)
# 		else:
# 			return response
#
# 	def form_valid(self,form):
#
# 		response = super(AjaxMixin,self).form_valid(form)
# 		if self.request.is_ajax():
# 			data={'pk':self.object.pk,}
# 			return self.render_to_json_response(data)
# 		else:
# 			return response


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
