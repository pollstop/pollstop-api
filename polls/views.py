from rest_framework import viewsets

from . import models, serializers


class PollViewSet(viewsets.ModelViewSet):
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer
