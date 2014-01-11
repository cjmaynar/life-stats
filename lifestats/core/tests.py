from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from django.contrib.auth.models import User

class RegisterTest(TestCase):
    def test_register(self):
        client = Client()
        args = {
            'username': 'newUser',
            'password': 'newPass'
        }
        response = client.post(reverse('register'), args)
        self.assertEquals(response.status_code, 302)

        try:
            user = User.objects.get(username="newUser")
        except DoesNotExist:
            self.fail("No user created")

        # Ensure the user's password was hashed
        self.assertNotEqual(user.password, 'newPass')
