from django.db import models


class Categoria(models.Model):
    descricao: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.descricao
