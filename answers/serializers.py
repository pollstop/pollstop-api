from rest_framework import serializers

from . import models


class AnswerSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'type',
            'id',
            'content',
            'created_at',
            'vote_count',
        )
        model = models.Answer

    def get_type(self, answer):
        return 'answer'
