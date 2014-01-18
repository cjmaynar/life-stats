from django.conf.urls import patterns, url

from .views import Events, EventDetail, EventData, CreateEvent, Typeahead

urlpatterns = patterns('',
    url(r'^$', Events.as_view(), name='events'),
    url(r'^(?P<pk>[0-9]*)/$', EventDetail.as_view(), name='event_detail'),
    url(r'^create$', CreateEvent.as_view(), name='event_create'),
    url(r'^data/$', EventData.as_view(), name='event_data'),
    url(r'^typeahead/$', Typeahead.as_view(), name='typeahead'),
)
