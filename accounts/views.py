from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models, serializers


class UserViewSet(mixins.CreateModelMixin,
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
        else: # use public serializer
            serializer = serializers.PublicUserSerializer(user)
            return Response(serializer.data)
