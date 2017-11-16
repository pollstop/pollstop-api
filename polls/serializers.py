from rest_framework import serializers
from . import models
from accounts.models import User


class PollSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    choices = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'type',
            'id',
            'title',
            'description',
            'date_created',
            'owner',
            'choices',
            'tags',
        )
        model = models.Question

    def get_type(self, question):
        return 'poll'

    def get_choices(self, question):
        choices = models.Choice.objects.filter(question_id=question.id)
        serializer = ChoiceSerializer(choices, many=True)
        return serializer.data


class ChoiceSerializer(serializers.ModelSerializer):
    votes = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'text',
            'votes',
        )
        model = models.Choice

    def get_votes(self, choice):
        return User.objects.all().filter(votes__in=[choice]).count()
