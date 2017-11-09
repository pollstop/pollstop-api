from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=320, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_voted_at = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField('tags.Tag', blank=True)
    answers = models.ManyToManyField('answers.Answer')

    class Meta:
        ordering = [ '-created_at', 'title', ]

    def __str__(self):
        return self.title
