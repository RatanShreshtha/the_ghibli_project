from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import exceptions, mixins, response, viewsets
from rest_framework_api_key.permissions import HasAPIKey

from .models import Film, People
from .serializers import FilmSerializer, PeopleSerializer


class FilmViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows Films to be viewed or edited.
    """

    queryset = Film.objects.all().order_by("-release_date").prefetch_related("people", "people__specie")
    serializer_class = FilmSerializer
    permission_classes = [HasAPIKey]

    @method_decorator(cache_page(1 * 60))
    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        film = queryset.filter(id=pk).first()
        if film is None:
            raise exceptions.NotFound()
        serializer = FilmSerializer(film)
        return response.Response(serializer.data)


class PeopleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows People to be viewed or edited.
    """

    queryset = People.objects.all().order_by("name").prefetch_related("specie")
    serializer_class = PeopleSerializer
    permission_classes = [HasAPIKey]

    @method_decorator(cache_page(1 * 60))
    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        people = queryset.filter(id=pk).first()
        if people is None:
            raise exceptions.NotFound()
        serializer = PeopleSerializer(people)
        return response.Response(serializer.data)
