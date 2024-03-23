from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from livraria.models import Categoria
from livraria.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # busca pelo(s) campo(s) declarado(s)
    # ex.: descricao=Fantasia
    filterset_fields = ["descricao"]
    # busca quando usar o search=Fantasia
    search_fields = ["descricao"]
    # possíveis filtros
    ordering_fields = ["descricao"]
    # filtro padrão
    ordering = ["descricao"]
