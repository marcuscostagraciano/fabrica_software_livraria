from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

from livraria.models import Autor, Categoria, Editora, Livro
from livraria.serializers import (AutorSerializer, CategoriaSerializer,
                                  EditoraSerializer, LivroSerializer,
                                  LivroDetailSerializer, LivroListSerializer)


# Create your views here.
class CategoriaViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        if self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
