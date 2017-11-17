from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated
from . import models, serializers


class UserViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def retrieve(self, request, pk=None):
        queryset = models.User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        if user == request.user:
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data)
        else:  # use public serializer
            serializer = serializers.PublicUserSerializer(user)
            return Response(serializer.data)

    def create(self, request):
        # TODO: Override create method
        # http://www.django-rest-framework.org/api-guide/viewsets/
        # validate fields and creat a new user
        # Make sure create a new token for new user
        # http://www.django-rest-framework.org/api-guide/authentication/
        pass

    def update(self, request, pk=None):
        # TODO: Override update method
        # http://www.django-rest-framework.org/api-guide/viewsets/
        # validate fields and update user with given pk
        pass

    # detail route to return token for user
    # .../users/<user_id>/token
    @detail_route(methods=['get'])
    def token(self, request, pk=None):
        # TODO: Validate email and password fields are included in the request,
        # check if a user with given info exists, and return user's token.
        pass

    # list route to return all polls for user
    # .../users/<user_id>/polls
    @list_route(methods=['get'])
    def token(self, request, pk=None):
        # TODO: return all polls owned by given user
        pass
