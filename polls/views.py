from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models, serializers


class PollViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    queryset = models.Question.objects.all()
    serializer_class = serializers.PollSerializer

    # list route to return latest polls
    # .../polls/latest
    @list_route()
    def latest(self, request):
        latest_polls = models.Question.objects.order_by('-date_created')[:10]
        serializer = self.get_serializer(latest_polls, many=True)
        return Response(serializer.data)


class ChoiceViewSet(mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = models.Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer

    @detail_route(['put'])
    def vote(self, request, pk=None):
        choice = self.get_object()
        user = request.user
        user.votes.add(choice)
        user.save()
        serializer = self.get_serializer(choice)
        return Response(serializer.data)

    @detail_route(['put'])
    def unvote(self, request, pk=None):
        choice = self.get_object()
        user = request.user
        user.votes.remove(choice)
        user.save()
        serializer = self.get_serializer(choice)
        return Response(serializer.data)
