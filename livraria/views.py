from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria, Editora
from livraria.serializers import CategoriaSerializer, EditoraSerializer


# Create your views here.
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
