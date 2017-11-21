from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from django.db import models
from django.utils import timezone
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def create_user(self, email, display_name=None, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        if not display_name:
            display_name = email

        user = self.model(
            email=self.normalize_email(email),
            display_name=display_name
        )
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=user)
        token.save()
        return user

    def create_superuser(self, email, display_name, password):

        if not display_name:
            display_name = email

        user = self.create_user(
            email,
            display_name,
            password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=140)
    bio = models.CharField(max_length=140, blank=True, default='')
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    votes = models.ManyToManyField('polls.Choice', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['display_name', ]

    def __str__(self):
        return '{}'.format(self.email)

    def get_short_name(self):
        return '{}'.format(self.display_name)

    def get_long_name(self):
        return '{} ({})'.format(self.display_name, self.email)
