from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from livraria.models import Livro
from livraria.serializers import (LivroSerializer, LivroDetailSerializer,
                                  LivroListSerializer)


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["categoria__descricao", "editora__nome"]
    search_fields = ["titulo"]

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        if self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
