from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.test import TestCase, Client

class HomeTest(TestCase):
    client = Client()
    user = None

    @classmethod
    def setUpClass(cls):
        try:
            cls.user = User.objects.create_user(username='test', password='test')
        except IntegrityError:
            pass

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        learn = "Learn Your Habbits"
        self.assertTrue(learn in response.content)

        self.client.login(username='test', password='test')
        response = self.client.get(reverse('home'))
        self.assertTrue("My Stats" in response.content)
