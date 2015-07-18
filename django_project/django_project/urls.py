from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.static import *
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django_project.views.home', name='home'),
    (r'^tinymce/', include('tinymce.urls')),
    # url(r'^blog/', include('blog.urls')),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^eventos/$', 'events.views.events_list', name='events_list'),
    url(r'^riders/fmx/$', 'riders.views.riders_fmx_list', name='riders_fmx_list'),
    url(r'^riders/bmx/$', 'riders.views.riders_bmx_list', name='riders_bmx_list'),
    url(r'^contacto/$', 'contact.views.contact', name='contact'),
    url(r'^blogs/$', 'django_project.views.home', name='home'),
    url(r'^riders/fmx/(?P<rider>[\w.@+-]+)/$', 'riders.views.rider', name='rider'),
    url(r'^riders/bmx/(?P<rider>[\w.@+-]+)/$', 'riders.views.rider', name='rider'),
    url(r'^eventos/(?P<event>[\w.@+-]+)/$', 'events.views.event', name='event'),
    url(r'^blogs/(?P<post>[\w.@+-]+)/$', 'blogs.views.post', name='post'),
)
