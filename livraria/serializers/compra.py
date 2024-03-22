from rest_framework.serializers import (ModelSerializer,
                                        CharField,
                                        SerializerMethodField)

from livraria.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ["livro", "quantidade", "total"]
        depth = 2

    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.quantidade * instance.livro.preco


class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"

    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)
