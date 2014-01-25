import json

from braces.views import LoginRequiredMixin

from django.core.urlresolvers import reverse
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, FormView

from .models import Event, Occurence, Category
from .forms import CreateEventForm, AddOccuranceForm

class Events(LoginRequiredMixin, ListView):
    '''Some basic info about all a user's events'''
    template_name = "events.html"
    model = Event

    def get_context_data(self, **kwargs):
        context = super(Events, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(user=self.request.user)
        return context


class EventData(LoginRequiredMixin, View):
    def get(self, request):
        events = Event.objects.filter(user=request.user)

        data = {}
        data['key'] = 'Frequent Events'
        data['values'] = [{'label': e.name, 'value': e.occurrences.count()} for e in events]
        return HttpResponse(json.dumps([data]), content_type="application/json")


class EventDetail(LoginRequiredMixin, View):
    '''See the detailed information for a specific event'''
    template_name = "event_detail.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context['event'] = Event.objects.get(pk=self.kwargs.get('pk'))
        context['form'] = AddOccuranceForm()
        return render(request, self.template_name, context)


class CreateEvent(LoginRequiredMixin, CreateView):
    '''Used to generate new events'''
    template_name = "create_event.html"
    model = Event
    form_class = CreateEventForm
    success_url = '/events'

    def get_initial(self):
        return { 'user': self.request.user }

class Typeahead(LoginRequiredMixin, View):
    '''A AJAX view for generating the Typeahead dropdown'''
    def get(self, request):
        data = [c.name for c in Category.objects.all()]
        return HttpResponse(json.dumps(data), content_type="application/json")
