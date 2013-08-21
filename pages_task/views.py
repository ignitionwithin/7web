from django.views.generic import TemplateView


class Greeting(TemplateView):
    """
    Select html template for greeting page
    """
    template_name = 'greeting.html'
