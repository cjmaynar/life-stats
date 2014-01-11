import datetime
import re

from django import forms
from django.contrib.auth.models import User

from .models import Event, Occurence, Category

class CreateEventForm(forms.ModelForm):
    user = forms.ModelChoiceField(widget=forms.widgets.HiddenInput, queryset=User.objects.all())
    occurrences = forms.CharField()
    category = forms.CharField(widget=forms.TextInput(attrs={'class': 'typeahead'}))
    
    def clean_occurrences(self):
        data = self.cleaned_data['occurrences']
        try:
            date = datetime.datetime.strptime(data, '%m/%d/%Y')
        except ValueError:
            raise forms.ValidationError("Incorrect date format")

        return Occurence.objects.get_or_create(date=date)[0]
        
    def clean_category(self):
        category = self.cleaned_data['category']
        if not re.match('^[a-zA-Z0-9]*$', category):
            raise forms.ValidationError("Invalid category name")

        return Category.objects.get_or_create(name=category)[0]

    class Meta():
        model = Event
