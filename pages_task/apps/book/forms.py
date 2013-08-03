from django import forms
from models import TextNote
class AddNoteForm(forms.ModelForm):
	note_value=forms.CharField(
		min_length=10,
		widget=forms.Textarea(attrs={'cols': 60, 'rows': 20}))
	class Meta:
		model = TextNote
		fields = ['note_name','note_value','note_image','note_book']

	class Media:
		js = ('//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js',
		'/media/js/counter.js',)
