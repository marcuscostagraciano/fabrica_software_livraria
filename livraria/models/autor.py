from django.db import models


class Autor(models.Model):
    nome: str = models.CharField(max_length=255)
    email: str = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
