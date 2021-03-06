import datetime
import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms
from django.contrib.auth.models import User

from .models import Event, Occurence, Category

class CreateEventForm(forms.ModelForm):
    name = forms.CharField(label="Description", help_text="What did you do?")
    user = forms.ModelChoiceField(widget=forms.widgets.HiddenInput, queryset=User.objects.all())
    occurrences = forms.CharField(label="Date of event", help_text="When did you do this?")
    category = forms.CharField(widget=forms.TextInput(attrs={'class': 'typeahead'}), help_text="What type of thing is this?")

    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'create_event'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create'))
    
    def clean_occurrences(self):
        data = self.cleaned_data['occurrences']
        try:
            date = datetime.datetime.strptime(data, '%m/%d/%Y')
        except ValueError:
            raise forms.ValidationError("Incorrect date format")

        return [Occurence.objects.get_or_create(date=date)[0]]
        
    def clean_category(self):
        category = self.cleaned_data['category']
        if not re.match('^[a-zA-Z0-9 ]*$', category):
            raise forms.ValidationError("Invalid category name")

        return Category.objects.get_or_create(name=category)[0]

    class Meta:
        model = Event
        exclude = ('slug',)


class AddOccuranceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddOccuranceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'add_occurance'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add'))

    class Meta:
        model = Occurence
