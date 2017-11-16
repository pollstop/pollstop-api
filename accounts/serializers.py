from rest_framework import serializers
from . import models


class PublicUserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'type',
            'id',
            'email',
        )
        model = models.User

    def get_type(self, user):
        return 'user'


class UserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'type',
            'id',
            'email',
            'votes',
        )
        model = models.User

    def get_type(self, user):
        if user.is_superuser:
            return 'superuser'
        elif user.is_staff:
            return 'staff'
        else:
            return 'user'
