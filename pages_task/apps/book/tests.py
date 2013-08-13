from django_webtest import WebTest
from models import TextNote, Book

class MyTestCase(WebTest):
	""" test primary project functional	"""
	fixtures = ['fixture.json',]

	def test_greeting_page(self):
		""" test root page exists  """
		greeting = self.app.get('/')
		assert 'Here is my ' in greeting

	def test_notes_page_exist(self):
		""" this function tests, that pages with notes exists """
		resp = self.app.get('/book/')
		assert '200 OK' == resp.status

	def test_add_note_exists(self):
		""" this function covers ability to go on note's create page  """
		resp = self.app.get('/')
		next_step = self.app.get(resp.click('app').location)
		form=next_step.forms['add_new_note']
		assert form.submit()
		assert form.submit().status == '200 OK'

	def test_add_note_form_min_char_limit(self):
		""" this function test minimum 10 chars condition """
		resp = self.app.get('/book/create_note/')
		forms= resp.forms
		main_form=forms['main_form']
		main_form['name'].value='some te4xt'
		main_form['value'].value = 'NineChars'
		res=main_form.submit()
		assert 'Ensure this value has at least 10 characters' in res

	def test_add_note_form_normal_char_limit(self):
		"""
		this function tests ability to create note
		"""
		resp = self.app.get('/book/create_note/')
		forms= resp.forms
		main_form=forms['main_form']
		main_form['name'].value='some text'
		main_form['value'].value = 'My ten Chars'
		res=main_form.submit('Add note')
		assert '200 OK' == res.status

	def test_custom_template_tag_exists(self):
		"""
		test , that required custom template tag exists, and show valid information
		"""
		index_page_resp  = self.app.get('/book/')
		create_page_resp = self.app.get('/book/create_note/')
		value_1 = str(index_page_resp.html.h4).strip('<h4>').strip('</h4>')
		value_2 = str(create_page_resp.html.h4).strip('<h4>').strip('</h4>')
		assert value_1 == value_2
		assert int(value_2[-1]) and int(value_1[-1])


	def test_objects_on_list_page(self):
		"""
		this function tests - ability to show valid notes list on note's list page
		"""
		page = self.app.get('/book/')
		db_objects = TextNote.objects.all()
		obj = db_objects[0]
		assert obj.name in page
