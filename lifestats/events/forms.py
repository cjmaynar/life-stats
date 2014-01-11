from django import forms
from django.contrib.auth.models import User

from .models import Event

class CreateEventForm(forms.ModelForm):
    user = forms.ModelChoiceField(widget=forms.widgets.HiddenInput, queryset=User.objects.all())

    class Meta():
        model = Event
