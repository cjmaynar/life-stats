from django.conf.urls import patterns, url

from .views import Events, EventDetail, EventData, CreateEvent, Typeahead, EventCategories, EventCategory

urlpatterns = patterns('',
    url(r'^$', Events.as_view(), name='events'),
    url(r'^(?P<pk>[0-9]*)/$', EventDetail.as_view(), name='event_detail'),
    url(r'^create$', CreateEvent.as_view(), name='event_create'),
    url(r'^categories/$', EventCategories.as_view(), name='event_categories'),
    url(r'^category/(?P<slug>[a-zA-Z0-9\-]*)/$', EventCategory.as_view(), name="event_category"),
    url(r'^data/$', EventData.as_view(), name='event_data'),
    url(r'^typeahead/$', Typeahead.as_view(), name='typeahead'),
)
