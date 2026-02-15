from django.shortcuts import render
from .models import Book
from .serializer import BookSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class BookViewSet(ModelViewSet):
    serializer_class=BookSerializer
    queryset=Book.objects.all()