from django.db import models
from django.conf import settings


class Question(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=320, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    tags = models.ManyToManyField('tags.Tag', blank=True)

    class Meta:
        ordering = ['-date_created', 'title', ]

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Question {} | {}'.format(self.question.id, self.text)
