from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from livraria.models import Autor
from livraria.serializers import AutorSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # busca vai usar o que estiver declarado aqui
    # ex.: email=jrrtolkien@oxford.uk
    filterset_fields = ["nome", "email"]
    # busca quando usar o search=jrrtolkien@oxford.uk
    search_fields = ["email"]
