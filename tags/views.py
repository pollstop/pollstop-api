from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from . import models, serializers


class TagViewSet(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):

    permission_classes = (AllowAny,)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer

    # list route to return polls for given tag
    # .../tags/<tag_id>/polls
    @list_route()
    def polls(self, request):
        # example: https://github.com/omaralbeik/omaralbeik.com-api/blob/master/tags/views.py#L44
        pass
