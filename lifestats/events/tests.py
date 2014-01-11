import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from .models import Event, Occurence, Category

class EventTest(TestCase):
    client = Client()
    user = None

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username='test', password='test')
        today = datetime.date.today()

        event = Event()
        event.user = cls.user
        event.name = "First Event"
        event.category = Category.objects.create(name="FirstCategory")
        event.occurrences = Occurence.objects.create(date=today)
        event.save()

    def setUp(self):
        self.client.login(username='test', password='test')

    def test_events_view(self):
        response = self.client.get(reverse('events'))
        self.assertTrue(response.status_code, 200)

    def test_event_detail(self):
        event = Event.objects.first()
        data = { 'pk': event.id }
        response = self.client.get(reverse('event_detail', kwargs=data))
        self.assertTrue(response.status_code, 200)

    def test_create_event(self):
        data = {
            'user' : self.user.id,
            'name' : 'TestEvent',
            'occurences': '2014-1-1',
            'category': 'TestCategory'
        }

        response = self.client.post(reverse('event_create'), data)
        self.assertTrue(response.status_code, 302)
