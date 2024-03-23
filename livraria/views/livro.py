from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from livraria.models import Livro
from livraria.serializers import (LivroSerializer, LivroDetailSerializer,
                                  LivroListSerializer)


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # busca pelo(s) campo(s) declarado(s)
    filterset_fields = ["categoria__descricao", "editora__nome"]
    # busca quando usar o search=
    search_fields = ["titulo"]
    # possíveis filtros
    ordering_fields = ["titulo", "preco"]
    # filtro padrão
    ordering = ["titulo"]

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        if self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
