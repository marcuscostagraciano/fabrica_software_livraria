from django.db import models

from typing import Final

from usuario.models import Usuario
from .livro import Livro

# Status da compra lookup table
COMPRA_STATUS_DICT: Final[dict[int, str]] = {
    1: "Carrinho",
    2: "Realizado",
    3: "Pago",
    4: "Entregue"
}
# Tipos de pagamento lookup table
TIPO_PAGAMENTO_DICT: Final[dict[int, str]] = {
    1: "Cartão de Crédito",
    2: "Cartão de Débito",
    3: "Pix",
    4: "Boleto",
    5: "Transferência Bancária",
    6: "Dinheiro",
    7: "Outro"
}


class Compra(models.Model):
    class TipoPagamento(models.IntegerChoices):
        CARTAO_CREDITO = 1, "Cartão de Crédito"
        CARTAO_DEBITO = 2, "Cartão de Débito"
        PIX = 3, "Pix"
        BOLETO = 4, "Boleto"
        TRANSFERENCIA_BANCARIA = 5, "Transferência Bancária"
        DINHEIRO = 6, "Dinheiro"
        OUTRO = 7, "Outro"

    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT,
                                related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices,
                                 default=StatusCompra.CARRINHO)
    tipo_pagamento = models.IntegerField(choices=TipoPagamento.choices,
                                         default=TipoPagamento.CARTAO_CREDITO)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (f"{self.usuario} - {COMPRA_STATUS_DICT[self.status]} "
                f"- {TIPO_PAGAMENTO_DICT[self.tipo_pagamento]}")

    @property
    def total(self):
        return sum(item.preco_item * item.quantidade
                   for item in self.itens.all())


class ItensCompra(models.Model):
    compra: Compra = models.ForeignKey(Compra, on_delete=models.CASCADE,
                                       related_name="itens")
    livro: Livro = models.ForeignKey(Livro, on_delete=models.PROTECT,
                                     related_name="+")
    quantidade: int = models.IntegerField(default=1)
    preco_item: float = models.DecimalField(max_digits=10, decimal_places=2,
                                            default=0)

    def __str__(self) -> str:
        return f"{self.compra} - {self.livro}"
