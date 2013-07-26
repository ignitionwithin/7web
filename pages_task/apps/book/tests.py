from django_webtest import WebTest
from django.contrib.auth.models import User
from models import TextNote
class MyTestCase(WebTest):

	def setUp(self):
	#Users:
		self.user_1 = User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')
		self.user_2 = User.objects.create_user('Jim Carrey', 'jim@carrey.com', 'jimspassword')
	#Notes:
		self.note_1 = TextNote.objects.create(note_name='First', note_value='THIS is My Ten Chars')
		self.note_2 = TextNote.objects.create(note_name='Second', note_value='THIS is My Ten Chars')
	def testGreetingPage(self):
		greeting = self.app.get('/')
		assert 'Here is my ' in greeting

	def testNotesPageExist(self):
		resp = self.app.get('/book/')
		assert '200 OK' == resp.status

	def testAddNoteExist(self):
		resp = self.app.get('/')
		next_step = self.app.get((resp.click('app').location))
		form=next_step.forms['add_new_note']
		assert form.submit()
		assert form.submit().status == '200 OK'

	def testAddNoteFormMinCharLimit(self):
		resp = self.app.get('/book/create_note/')
		forms= resp.forms
		main_form=forms['main_form']
		main_form['note_name'].value='some te4xt'
		main_form['note_value'].value = 'NineChars'
		res=main_form.submit()
		assert 'Ensure this value has at least 10 characters' in res

	def testAddNoteFormNormalCharLimit(self):
		resp = self.app.get('/book/create_note/')
		forms= resp.forms
		main_form=forms['main_form']
		main_form['note_name'].value='some text'
		main_form['note_value'].value = 'My ten Chars'
		res=main_form.submit('Add note')
		assert '302 FOUND' == res.status

	def testCustomTemplateTagExist(self):
		index_page_resp  = self.app.get('/book/')
		create_page_resp = self.app.get('/book/create_note/')
		value_1 = str(index_page_resp.html.h4).strip('<h4>').strip('</h4>')
		value_2 = str(create_page_resp.html.h4).strip('<h4>').strip('</h4>')
		assert value_1 == value_2
		assert int(value_2[-1]) and int(value_1[-1])