from rest_framework import serializers

from . import models


class PollSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    #tags = serializers.SerializerMethodField()
    answers = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'type',
            'id',
            'title',
            'description',
            'created_at',
            'last_voted_at',
            'tags',
            'answers',
        )
        model = models.Poll

    def get_type(self, poll):
        return 'poll'

    def get_answers(self, poll):
        return poll.answers.values_list('content', flat=True)

    #def get_tags(self, poll):
    #    return poll.tags.values_list('name')
