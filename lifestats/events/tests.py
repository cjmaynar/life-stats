import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from .models import Event, Occurence, Category

class EventTest(TestCase):
    @classmethod
    def setUpClass(cls):
        User.objects.create(username='test', password='test')

    def test_event(self):
        user = User.objects.get(id=1)
        category = Category.objects.get_or_create(name='First Category')
        occurrence = Occurence.objects.get_or_create(date=datetime.date.today())

        event = Event()
        event.user = user
        event.name = "First"
        event.category = category[0]
        event.save()
        self.assertIsNotNone(event.pk)
        event.occurrences.add(occurrence[0])
        self.assertNotEqual(event.occurrences.all(), [])

    def test_events_view(self):
        client = Client()
        response = client.get(reverse('events'))
        self.assertTrue(response.status_code, 200)
