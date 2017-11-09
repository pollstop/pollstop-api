from rest_framework import serializers

from . import models


class PollSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

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
