from braces.views import LoginRequiredMixin

from django.shortcuts import render
from django.views.generic import TemplateView

class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile.html'
