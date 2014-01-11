from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from core.views import RegisterView
from .views import HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^accounts/register/$', RegisterView.as_view(), name='register'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', include('events.urls')),
    url(r'^users/', include('users.urls')),
)

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
