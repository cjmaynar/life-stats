from braces.views import LoginRequiredMixin

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from .models import Event, Occurence, Category
from .forms import CreateEventForm

class Events(LoginRequiredMixin, TemplateView):
    template_name = "events.html"

class CreateEvent(LoginRequiredMixin, CreateView):
    template_name = "create_event.html"
    model = Event
    form_class = CreateEventForm
    success_url = '/events'

    def get_initial(self):
        return { 'user': self.request.user }
