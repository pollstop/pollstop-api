from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from . import models, serializers


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
