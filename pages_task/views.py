from django.views.generic import TemplateView

class Greeting(TemplateView):
	template_name = 'greeting.html'