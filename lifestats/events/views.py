import json

from braces.views import LoginRequiredMixin

from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from django.contrib import messages
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
        context['events'] = Event.objects.filter(user=self.request.user)[:10]
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
        context['event'] = Event.objects.get(slug=self.kwargs.get('slug'))
        context['form'] = AddOccuranceForm()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        event = Event.objects.get(slug=self.kwargs.get('slug'))
        form = AddOccuranceForm(request.POST)
        if form.is_valid():
            occurence = form.save()
            event.occurrences.add(occurence)
            event.save()
            messages.success(request, "Date Added")

            # Reset the form for another date
            context['form'] = AddOccuranceForm()
        else:
            messages.error(request, "Invalid Form")
            context['form'] = form

        context['event'] = event
        return render(request, self.template_name, context)


class CreateEvent(LoginRequiredMixin, CreateView):
    '''Used to generate new events'''
    template_name = "create_event.html"
    model = Event
    form_class = CreateEventForm
    success_url = reverse_lazy('events')

    def get_initial(self):
        return { 'user': self.request.user }

    def form_valid(self, form):
        messages.success(self.request, "Event Created")
        return super(CreateEvent, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid Form")
        return super(CreateEvent, self).form_invalid(form)

class Typeahead(LoginRequiredMixin, View):
    '''A AJAX view for generating the Typeahead dropdown'''
    def get(self, request):
        data = [c.name for c in Category.objects.all()]
        return HttpResponse(json.dumps(data), content_type="application/json")


class EventCategories(LoginRequiredMixin, ListView):
    '''Some basic info about all a user's events'''
    template_name = "event_categories.html"
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventCategories, self).get_context_data(**kwargs)
        events = Event.objects.select_related().filter(user=self.request.user).order_by('category__name')
        context['categories'] = set([e.category for e in events])
        return context

class EventCategory(LoginRequiredMixin, DetailView):
    template_name = "event_category.html"
    model = Category
