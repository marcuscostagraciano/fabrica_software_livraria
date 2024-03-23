from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from livraria.models import Editora
from livraria.serializers import EditoraSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # busca vai usar o que estiver declarado aqui
    # ex.: nome=Novatec
    filterset_fields = ["nome", "site"]
    # busca quando usar o search=Novatec
    search_fields = ["nome"]
