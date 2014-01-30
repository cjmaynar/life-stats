from autofixture import AutoFixture
from autofixture.generators import ChoicesGenerator, InstanceSelector
from optparse import make_option

from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from events.models import Event, Category, Occurence

class Command(BaseCommand):
    '''A management command powered by autofixture to generate random data
    for the application.'''
    option_list = BaseCommand.option_list + (
            make_option('--users', '-u', action='store', type='int', dest='users', default=5),
            make_option('--categories', '-c', action='store', type='int', dest='categories', default=20),
            make_option('--occurrences', '-o', action='store', type='int', dest='occurrences', default=20),
            make_option('--events', '-e', action='store', type='int', dest='events', default=20),
    )

    def handle(self, *args, **kwargs):
        self.stdout.write("Generating Data...")

        self.user_count = kwargs.get('users')
        self.event_count = kwargs.get('events')
        self.occurences_count = kwargs.get('occurrences')
        self.categories_count = kwargs.get('categories')

        # Create test users, or select them if they already exist
        users = []
        for k, v in enumerate(range(self.user_count)):
            try:
                user = User.objects.create_user(username='test%d' % (v), password='test')
            except IntegrityError:
                user = User.objects.get(username='test%d' % (v))
            users.append(user)

        ofixture = AutoFixture(Occurence)
        occurrences = ofixture.create(self.occurences_count)

        cfixture = AutoFixture(Category)
        categories = cfixture.create(self.categories_count)

        # Generators ensure each event has randomly chosen items
        values = {
            'user': ChoicesGenerator(values=users),
            'category': ChoicesGenerator(values=categories),
            'occurrences': InstanceSelector(Occurence.objects.get_query_set(), max_count=10, min_count=1),
        }
        efixture = AutoFixture(Event, field_values=values)
        events = efixture.create(self.event_count)

        self.stdout.write("Done")
