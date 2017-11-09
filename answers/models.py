from django.db import models


class Answer(models.Model):
    content = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    vote_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content
