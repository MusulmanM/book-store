from rest_framework.generics import ListCreateAPIView
from .models import Author
from .serializer import AuthorSerializer

# Create your views here.


class AuthorListCreateView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroyView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer