from django.conf.urls import patterns,url
from views import *

urlpatterns = patterns('',
					   url(r'^$',Notes_list.as_view(),name='notes_list'),
					   url(r'create_note/$',Add_note.as_view(),name='create_note'),
					   )