from rest_framework import serializers
from . import models
from accounts.models import User


class PollSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    choices = serializers.SerializerMethodField()

    choice_1 = serializers.CharField(write_only=True, default=None)
    choice_2 = serializers.CharField(write_only=True, default=None)
    choice_3 = serializers.CharField(write_only=True, default=None)
    choice_4 = serializers.CharField(write_only=True, default=None)

    class Meta:
        fields = (
            'type',
            'id',
            'title',
            'description',
            'date_created',
            'owner',
            'choices',
            'choice_1',
            'choice_2',
            'choice_3',
            'choice_4',
        )

        model = models.Question

    def validate(self, attrs):
        """
        Check that the question has at least 2 choices
        """
        choices = [
            attrs['choice_1'],
            attrs['choice_2'],
            attrs['choice_3'],
            attrs['choice_4'],
        ]
        numberOfChoices = sum(x is not None for x in choices)

        if numberOfChoices < 2:
            raise serializers.ValidationError("Question must have at least 2 choices")
        return attrs

    def create(self, validated_data):
        choice_1 = validated_data.pop('choice_1', None)
        choice_2 = validated_data.pop('choice_2', None)
        choice_3 = validated_data.pop('choice_3', None)
        choice_4 = validated_data.pop('choice_4', None)

        question = models.Question(**validated_data)
        question.save()

        for c in [choice_1, choice_2, choice_3, choice_4]:
            if c:
                choice = models.Choice(text=c, question=question)
                choice.save()

        return question

    def get_type(self, question):
        return 'poll'

    def get_choices(self, question):
        # get all choices for given question
        choices = models.Choice.objects.filter(question_id=question.id)
        serializer = ChoiceSerializer(choices, many=True)
        return serializer.data


class ChoiceSerializer(serializers.ModelSerializer):
    votes = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'id',
            'text',
            'votes',
        )
        model = models.Choice

    def get_votes(self, choice):
        # Iterate over all users and get vote counts for this choice
        return User.objects.all().filter(votes__in=[choice]).count()
