from django.conf.urls import patterns, url
from views import *


urlpatterns = patterns(
    #  describes projects url - view relation
    '',
    url(r'^$', NotesList.as_view(), name='notes_list'),
    url(r'create_note/$', AddNote.as_view(), name='create_note'),
    url(r'widget/$', PortableWidget.as_view()),
    )
