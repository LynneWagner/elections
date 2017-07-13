from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    slug = models.SlugField(blank=True)
    next_question = models.ForeignKey('self', null=True)

    def __str__(self):
        return self.question_text

    @property
    def name(self):
        return self.question_text

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Question, self).save(*args, **kwargs)

class Choice(models.Model):
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    username = models.URLField(blank=True)
    address = models.TextField()

    def __str__(self):
        return self.user.username
