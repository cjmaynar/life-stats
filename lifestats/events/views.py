import json

from braces.views import LoginRequiredMixin

from django.core.urlresolvers import reverse
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView

from .models import Event, Occurence, Category
from .forms import CreateEventForm

class Events(LoginRequiredMixin, ListView):
    template_name = "events.html"
    model = Event

    def get_context_data(self, **kwargs):
        context = super(Events, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(user=self.request.user)
        return context


class EventDetail(LoginRequiredMixin, DetailView):
    template_name = "event_detail.html"
    model = Event


class CreateEvent(LoginRequiredMixin, CreateView):
    template_name = "create_event.html"
    model = Event
    form_class = CreateEventForm
    success_url = '/events'

    def get_initial(self):
        return { 'user': self.request.user }

class Typeahead(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        data = []
        for category in categories:
            data.append(category.name)


        return HttpResponse(json.dumps(data), content_type="application/json")
