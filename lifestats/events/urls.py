from django.conf.urls import patterns, url

from .views import Events, CreateEvent

urlpatterns = patterns('',
    url(r'^$', Events.as_view(), name='events'),
    url(r'^create$', CreateEvent.as_view(), name='event_create'),
)
