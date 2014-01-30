from autofixture import AutoFixture
from autofixture.generators import ChoicesGenerator, InstanceSelector
from random import choice, randrange

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from events.models import Event, Category, Occurence

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        users = []
        for k, v in enumerate(range(5)):
            user = User.objects.create_user(username='test%d' % (v), password='test')
            users.append(user)

        ofixture = AutoFixture(Occurence)
        occurrences = ofixture.create(20)

        cfixture = AutoFixture(Category)
        categories = cfixture.create(20)

        values = {
            'user': ChoicesGenerator(values=users),
            'category': ChoicesGenerator(values=categories),
            'occurrences': InstanceSelector(Occurence.objects.get_query_set(), max_count=10, min_count=1),
        }
        efixture = AutoFixture(Event, field_values=values)
        events = efixture.create(20)

        self.stdout.write("Data Generated")
