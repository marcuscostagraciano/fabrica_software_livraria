from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from livraria.models import Categoria
from livraria.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # busca vai usar o que estiver declarado aqui
    # ex.: descricao=Fantasia
    filterset_fields = ["descricao"]
    # busca quando usar o search=Fantasia
    search_fields = ["descricao"]
