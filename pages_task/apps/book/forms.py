from django import forms
from models import TextNote
from ajax_upload.widgets import AjaxClearableFileInput

class AddNoteForm(forms.ModelForm):
	note_value=forms.CharField(
		min_length=10,
		widget=forms.Textarea(attrs={'cols': 60, 'rows': 20}))

	note_image = forms.ImageField(widget=AjaxClearableFileInput())
	class Meta:
		model = TextNote
		fields = ['note_name','note_value','note_image','note_book']

	class Media:
		js = ('//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js',
		'/media/js/counter.js',
		'ajax_upload/css/ajax-upload-widget.css',
		'ajax_upload/js/jquery.iframe-transport.js',
		'ajax_upload/js/ajax-upload-widget.js',
		)
