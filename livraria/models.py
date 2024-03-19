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

class Autor(models.Model):
    nome: str = models.CharField(max_length=255)
    email: str = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Livro(models.Model):
    titulo: str = models.CharField(max_length=255)
    isbn: str = models.CharField(max_length=32, null=True, blank=True)
    quantidade: int = models.IntegerField(default=0, null=True, blank=True)
    preco: float = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria: Categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora: Editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )

    def __str__(self) -> str:
        return f"{self.titulo} ({self.quantidade})"
