from django import forms
from models import TextNote
class AddNoteForm(forms.ModelForm):
	note_value=forms.CharField(min_length=10,widget=forms.Textarea(attrs={'cols': 60, 'rows': 20}))
	class Meta:
		model = TextNote
		fields = ['note_name','note_value']
