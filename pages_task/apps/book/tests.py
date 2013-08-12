from django_webtest import WebTest
from django.contrib.auth.models import User
from models import TextNote, Book

class MyTestCase(WebTest):

	fixtures = ['fixture.json',]
	# def setUp(self):
	# #Users:
	# 	self.user_1 = User.objects.create_user(
	# 		'Chevy Chase', 'chevy@chase.com', 'chevyspassword'
	# 	)
	# 	self.user_2 = User.objects.create_user(
	# 		'Jim Carrey', 'jim@carrey.com', 'jimspassword'
	# 	)
	# #Notes:
	# 	self.note_1 = TextNote.objects.create(
	# 		note_name='First', note_value='THIS is My Ten Chars',
	# 		note_image='ss.aa'
	# 	)
	# 	self.note_2 = TextNote.objects.create(
	# 		note_name='Second', note_value='THIS is My Ten Chars',
	# 		note_image='ss.aa'
	# 	)
	# 	self.book_1 = Book.objects.create(
	# 		book_name = 'Test book'
	# 	)

	def test_greeting_page(self):
		greeting = self.app.get('/')
		assert 'Here is my ' in greeting

	def test_notes_page_exist(self):
		resp = self.app.get('/book/')
		assert '200 OK' == resp.status

	def test_add_note_exists(self):
		resp = self.app.get('/')
		next_step = self.app.get(resp.click('app').location)
		form=next_step.forms['add_new_note']
		assert form.submit()
		assert form.submit().status == '200 OK'

	def test_add_note_form_min_char_limit(self):
		resp = self.app.get('/book/create_note/')
		forms= resp.forms
		main_form=forms['main_form']
		main_form['note_name'].value='some te4xt'
		main_form['note_value'].value = 'NineChars'
		res=main_form.submit()
		assert 'Ensure this value has at least 10 characters' in res

	def test_add_note_form_normal_char_limit(self):
		resp = self.app.get('/book/create_note/')
		forms= resp.forms
		main_form=forms['main_form']
		main_form['note_name'].value='some text'
		main_form['note_value'].value = 'My ten Chars'
		res=main_form.submit('Add note')
		assert '200 OK' == res.status

	def test_custom_template_tag_exists(self):
		index_page_resp  = self.app.get('/book/')
		create_page_resp = self.app.get('/book/create_note/')
		value_1 = str(index_page_resp.html.h4).strip('<h4>').strip('</h4>')
		value_2 = str(create_page_resp.html.h4).strip('<h4>').strip('</h4>')
		assert value_1 == value_2
		assert int(value_2[-1]) and int(value_1[-1])

	#	This tests don't needed with ajax image loading implimentation
	#
	# def test_uploaded_img_exists(self):
	# 	index_page_resp = self.app.get('/book/').html
	# 	img_path=index_page_resp.img['src']
	# 	assert str(TextNote.note_image) in img_path
	#
	# def test_book_checkbox_exists(self):
	# 	resp = self.app.get('/book/create_note/')
	# 	obj = TextNote.objects.get(pk=1)
	# 	img_path = obj.note_image
	# 	print(str(img_path))
	# 	assert img_path in resp.content

	def test_objects_on_list_page(self):
		page = self.app.get('/book/')
		db_objects = TextNote.objects.all()
		obj = db_objects[0]
		assert obj.note_name in page
