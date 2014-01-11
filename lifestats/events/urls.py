from django.conf.urls import patterns, url

from .views import Events

urlpatterns = patterns('',
    url(r'^$', Events.as_view(), name='events'),
)
