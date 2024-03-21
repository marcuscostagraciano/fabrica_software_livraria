from django.db import models


class Editora(models.Model):
    nome: str = models.CharField(max_length=100)
    site: str = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nome
