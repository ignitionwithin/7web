from django.conf.urls import patterns,url
from views import Notes_list

urlpatterns = patterns('',
					   url(r'^$',Notes_list.as_view(),name='notes_list')
					   )