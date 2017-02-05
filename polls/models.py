from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
# Question and Choice.
# A Question has a question and a publication date.
# A Choice has two fields: the text of the choice and a vote tally.
#   Each Choice is associated with a Question.

@python_2_unicode_compatible
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    ############# this gives the wrong answer the future date is not recently published
    #def was_published_recently(self):
    #   return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    ############# Ran test, and we come up with this new solution
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    #the green/red check in published recently field
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    #Finally, note a relationship is defined, using ForeignKey.
    # That tells Django each Choice is related to a single Question.
    # Django supports all the common database relationships:
    #  many-to-one, many-to-many, and one-to-one.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text
