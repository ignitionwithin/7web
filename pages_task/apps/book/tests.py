from django_webtest import WebTest
from models import TextNote
from django.core.urlresolvers import reverse

class ImplementationTest(WebTest):
    """ Test primary project functional	"""
    fixtures = ['initial_data.json', ]

    def test_greeting_page(self):
        """ Test root page exists  """
        greeting = self.app.get(reverse('home'))
        assert 'Here is my ' in greeting

    def test_notes_page_exist(self):
        """ This function tests, that pages with notes exists """
        resp = self.app.get(reverse('home'))
        book_page = self.app.get(resp.click('app').location)
        assert '200 OK' == book_page.status

    def test_add_note_exists(self):
        """ This function covers ability to go on note's create page  """
        resp = self.app.get(reverse('home'))
        next_step = self.app.get(resp.click('app').location)
        form = next_step.forms['add_new_note']
        assert form.submit()
        assert form.submit().status == '200 OK'

    def test_add_note_form_min_char_limit(self):
        """ This function test minimum 10 chars condition """
        resp = self.app.get(reverse('home'))
        book_page = self.app.get(resp.click('app').location)
        add_new_note_button= book_page.form
        create_page = add_new_note_button.submit()
        forms = create_page.forms
        main_form = forms['main_form']
        main_form['name'].value = 'some te4xt'
        main_form['value'].value = 'NineChars'
        res = main_form.submit()
        assert 'Ensure this value has at least 10 characters' in res

    def test_add_note_form_normal_char_limit(self):
        """
        This function tests ability to create note
        """
        resp = self.app.get(reverse('home'))
        book_page = self.app.get(resp.click('app').location)
        add_new_note_button= book_page.form
        create_page = add_new_note_button.submit()
        forms = create_page.forms
        main_form = forms['main_form']
        main_form['name'].value = 'some text'
        main_form['value'].value = 'My ten Chars'
        res = main_form.submit('Add note')
        assert '200 OK' == res.status

    def test_custom_template_tag_exists(self):
        """
        Test , that required custom template tag exists,
        and show valid information
        """
        resp = self.app.get(reverse('home'))
        book_page = self.app.get(resp.click('app').location)
        add_new_note_button= book_page.form
        create_page = add_new_note_button.submit()
        value_1 = str(book_page.html.h4).strip('<h4>').strip('</h4>')
        value_2 = str(create_page.html.h4).strip('<h4>').strip('</h4>')
        assert value_1 == value_2
        assert int(value_2[-1]) and int(value_1[-1])

    def test_objects_on_list_page(self):
        """
        This function tests - ability to show valid
        notes list on note's list page
        """
        resp = self.app.get(reverse('home'))
        book_page = self.app.get(resp.click('app').location)
        db_objects = TextNote.objects.all()
        for i in db_objects:
            assert i.name in book_page
