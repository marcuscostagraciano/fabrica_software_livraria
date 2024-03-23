from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from livraria.models import Compra
from livraria.serializers import CompraSerializer, CriarEditarCompraSerializer
from usuario.models import Usuario


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # busca pelo(s) campo(s) declarado(s)
    # ex.: status=(1, 2, 3 ou 4)
    filterset_fields = ["usuario", "status", "data"]
    # busca quando usar o search=
    search_fields = ["status"]
    # possíveis filtros
    ordering_fields = ["usuario", "status", "data"]
    # filtro padrão
    ordering = ["usuario"]

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all()
        elif usuario.groups.filter(name="Administradores"):
            return Compra.objects.all()
        elif usuario.tipo == Usuario.TipoUsuario.GERENTE:
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)

    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return CriarEditarCompraSerializer
        return CompraSerializer
