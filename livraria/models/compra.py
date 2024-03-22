from django.db import models

from usuario.models import Usuario
from .livro import Livro

compra_status_dict: dict[int, str] = {
    1: "Carrinho",
    2: "Realizado",
    3: "Pago",
    4: "Entregue"
}


class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)

    def __str__(self) -> str:
        return f"{self.usuario} - {compra_status_dict[self.status]}"


class ItensCompra(models.Model):
    compra: Compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    livro: Livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="+")
    quantidade: int = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.compra} - {self.livro}"
