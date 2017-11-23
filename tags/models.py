from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=80, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    #questions = models.ManyToManyField('polls.Question', blank=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name
