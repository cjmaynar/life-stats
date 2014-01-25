import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from .models import Event, Occurence, Category

class EventTest(TestCase):
    client = Client()
    fixtures = [
        'users/fixtures/initial_data.json',
        'events/fixtures/initial_data.json',
    ]

    def setUp(self):
        self.client.login(username='test', password='test')

    def test_events_view(self):
        response = self.client.get(reverse('events'))
        self.assertTrue(response.status_code, 200)

    def test_event_detail(self):
        event = Event.objects.first()
        data = { 'slug': event.slug }
        response = self.client.get(reverse('event_detail', kwargs=data))
        self.assertTrue(response.status_code, 200)

    def test_create_event(self):
        user = User.objects.get(username='test')
        data = {
            'user' : user.id,
            'name' : 'TestEvent',
            'occurrences': '01/01/2014',
            'category': 'TestCategory'
        }

        response = self.client.post(reverse('event_create'), data)
        self.assertEqual(Event.objects.all().count(), 3)
