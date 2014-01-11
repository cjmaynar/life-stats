from django.shortcuts import render

from django.views.generic import TemplateView, CreateView

from .models import Event
from .forms import CreateEventForm


class Events(TemplateView):
    template_name = "events.html"

class CreateEvent(CreateView):
    template_name = "create_event.html"
    model = Event
    form_class = CreateEventForm
