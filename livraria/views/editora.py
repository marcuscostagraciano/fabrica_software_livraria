from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from livraria.models import Editora
from livraria.serializers import EditoraSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # busca pelo(s) campo(s) declarado(s)
    # ex.: nome=Novatec
    filterset_fields = ["nome", "site"]
    # busca quando usar o search=Novatec
    search_fields = ["nome"]
    # possíveis filtros
    ordering_fields = ["nome", "site"]
    # filtro padrão
    ordering = ["nome"]
