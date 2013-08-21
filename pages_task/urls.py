from django.conf.urls import patterns, include, url
import views
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
                       #  describes how requested url related to view class
                       url(r'^$', views.Greeting.as_view(), name='home'),
                       url(r'^admin/doc/',
                           include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^book/',
                           include('pages_task.apps.book.urls',
                                   namespace='book'))
                       )
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                           (r'^media/(?P<path>.*)$',
                            'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT}))

urlpatterns += patterns('',
                        (r'^ajax-upload/', include('ajax_upload.urls')),
                        )
