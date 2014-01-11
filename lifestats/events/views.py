from django.shortcuts import render

from django.views.generic import TemplateView

class Events(TemplateView):
    template_name="events.html"

