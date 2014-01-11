import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from .models import Event, Occurence, Category

class EventTest(TestCase):
    @classmethod
    def setUpClass(cls):
        User.objects.create_user(username='test', password='test')

    def test_event(self):
        user = User.objects.get(id=1)
        category = Category.objects.get_or_create(name='First Category')
        occurrence = Occurence.objects.get_or_create(date=datetime.date.today())

        event = Event()
        event.user = user
        event.name = "First"
        event.category = category[0]
        event.occurrences = occurrence[0]
        event.save()
        self.assertIsNotNone(event.pk)

    def test_events_view(self):
        client = Client()
        response = client.get(reverse('events'))
        self.assertTrue(response.status_code, 200)

    def test_create_event(self):
        user = User.objects.get(username='test')
        data = {
            'user' : user.id,
            'name' : 'TestEvent',
            'occurences': '2014-1-1',
            'category': 'TestCategory'
        }

        client = Client()
        client.login(username='test', password='test')
        response = client.post(reverse('event_create'), data)
        self.assertTrue(response.status_code, 302)
