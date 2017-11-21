from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated, AllowAny
from . import models, serializers
import polls


class AuthViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)

    # detail route to return or create token for user
    # .../users/<user_id>/token
    @list_route(methods=['POST'])
    def token(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if not email:
            content = {'message': 'email field not found'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        if not password:
            content = {'message': 'password field not found'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        user = models.User.objects.get(email=email)
        if not user:
            content = {'message': 'user not found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            content = {'message': 'incorrect password'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)

        content = {'id': user.id, 'token': token.key}
        return Response(content, status=status.HTTP_200_OK)


class UserViewSet(mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        queryset = models.User.objects.all()
        # TODO: check this part for user not found case.
        user = get_object_or_404(queryset, pk=pk)

        if user == request.user:
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data)
        else:  # use public serializer
            serializer = serializers.PublicUserSerializer(user)
            return Response(serializer.data)

    # list route to return all polls for user
    # .../users/<user_id>/polls
    @detail_route(methods=['GET'])
    def polls(self, request, pk=None):
        user = self.get_object()
        questions = polls.models.Question.objects.all().filter(owner=user)
        serializer = polls.serializers.PollSerializer(questions, many=True)
        return Response(serializer.data)
