from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',views.Greeting.as_view(), name='home'),
    # url(r'^pages_task/', include('pages_task.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^book/',include('pages_task.apps.book.urls',namespace='book'))
)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

urlpatterns += patterns('',
    (r'^ajax-upload/', include('ajax_upload.urls')),
)