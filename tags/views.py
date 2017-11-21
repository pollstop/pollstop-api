from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . import models, serializers
import polls


class TagViewSet(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):

    permission_classes = (AllowAny,)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer

    # list route to return polls for given tag
    # .../tags/<tag_id>/polls
    @detail_route()
    def polls(self, request, pk=None):
        tag = self.get_object()
        questions = polls.models.Question.objects.all().filter(tags__in=[tag])
        serializer = polls.serializers.PollSerializer(questions, many=True)
        return Response(serializer.data)
