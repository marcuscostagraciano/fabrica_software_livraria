from django.db import models
from livraria.models import Autor, Categoria, Editora


class Livro(models.Model):
    titulo: str = models.CharField(max_length=255)
    isbn: str = models.CharField(max_length=32, null=True, blank=True)
    quantidade: int = models.IntegerField(default=0, null=True, blank=True)
    preco: float = models.DecimalField(max_digits=7, decimal_places=2,
                                       default=0, null=True, blank=True)
    categoria: Categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora: Editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )
    autores = models.ManyToManyField(Autor, related_name="livros")

    def __str__(self) -> str:
        return f"{self.titulo} ({self.quantidade})"
