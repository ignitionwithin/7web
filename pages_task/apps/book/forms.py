from django import forms
from models import TextNote
from ajax_upload.widgets import AjaxClearableFileInput


class AddNoteForm(forms.ModelForm):
    """
    This class override some model fields for requested model fields
    """
    value = forms.CharField(
        min_length=10,
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 20}))

    image = forms.ImageField(widget=AjaxClearableFileInput())

    class Meta:
        """
        This class selects needed model fields for form show
        """
        model = TextNote
        fields = ['name', 'value', 'image', 'book']

    class Media:
        """
        This class add required javascript to the form
        """
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js',
            '/media/js/counter.js',
            'ajax_upload/css/ajax-upload-widget.css',
            'ajax_upload/js/jquery.iframe-transport.js',
            'ajax_upload/js/ajax-upload-widget.js',
            )
