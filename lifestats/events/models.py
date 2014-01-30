from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

class Event(models.Model):
    '''Events are things that happen frequently in
    your life, examples are getting a haircut,
    buying groceries, or anything else you're
    curious how often you do'''
    user = models.ForeignKey(User)
    name = models.CharField(max_length=25, help_text="What did you do?")
    slug = models.SlugField(max_length=10)
    occurrences = models.ManyToManyField('Occurence', related_name="events", help_text="When did you do this?")
    category = models.ForeignKey('Category', related_name="events", help_text="What category does this belong to?")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unicode(self.name))
        return super(Event, self).save()

    def __unicode__(self):
        return self.name


class Occurence(models.Model):
    '''The dates you did this event'''
    date = models.DateField()

    class Meta:
        ordering = ['date']


class Category(models.Model):
    '''Events belong to a category, such as personal
    care, or something similar'''
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unicode(self.name))
        super(Category, self).save()

    def __unicode__(self):
        return self.name
