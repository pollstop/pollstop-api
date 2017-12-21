from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models


class PublicUserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'id',
            'type',
            'email',
            'display_name',
            'date_joined',
        )
        model = models.User

    def get_type(self, user):
        return 'user'


class UserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True, default=None)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if not password:
            raise serializers.ValidationError("User must have password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        fields = (
            'type',
            'id',
            'email',
            'display_name',
            'bio',
            'date_joined',
            'password',
            'token',
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

    def get_token(self, user):
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)

        return token.key
