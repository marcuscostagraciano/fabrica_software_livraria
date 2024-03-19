from django.db import models


# Create your models here.
class Categoria(models.Model):
    descricao: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.descricao

class Editora(models.Model):
    nome: str = models.CharField(max_length=100)
    site: str = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nome
