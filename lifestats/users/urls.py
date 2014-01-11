from django.conf.urls import patterns, include, url

from .views import UserProfile

urlpatterns = patterns('',
    url(r'^(?P<username>[a-zA-Z0-9]+)/$', UserProfile.as_view(), name="user_profile"),
)
