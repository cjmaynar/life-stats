from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    '''Events are things that happen frequently in
    your life, examples are getting a haircut,
    buying groceries, or anything else you're
    curious how often you do'''
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    occurrences = models.ManyToManyField('Occurence', related_name="events")
    category = models.ForeignKey('Category')


class Occurence(models.Model):
    '''The dates you did this event'''
    date = models.DateField()

    def __unicode__(self):
        return self.date.isoformat()


class Category(models.Model):
    '''Events belong to a category, such as personal
    care, or something similar'''
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
