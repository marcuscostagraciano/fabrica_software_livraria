from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from livraria.models import Autor
from livraria.serializers import AutorSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # busca pelo(s) campo(s) declarado(s)
    # ex.: email=jrrtolkien@oxford.uk
    filterset_fields = ["nome", "email"]
    # busca quando usar o search=jrrtolkien@oxford.uk
    search_fields = ["email"]
    # possíveis filtros
    ordering_fields = ["nome", "email"]
    # filtro padrão
    ordering = ["nome"]
