from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .models import User, Favorite
from books.models import Book
from .serializer import (
    UserSerializer, 
    RegisterSerializer, 
    LoginSerializer,
    FavoriteSerializer,
    FavoriteCreateSerializer,
    FavoriteListSerializer
)

# Create your views here.






class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        })


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Muvaffaqiyatli chiqildi"})




class FavoriteListView(generics.ListAPIView):
    serializer_class = FavoriteListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


class FavoriteCreateView(generics.CreateAPIView):
    serializer_class = FavoriteCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteDeleteView(generics.DestroyAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


class FavoriteDetailView(generics.RetrieveAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


class FavoriteToggleView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            book=book
        )
        
        if not created:
            favorite.delete()
            return Response({
                "message": "Kitob yoqqanlardan olib tashlandi",
                "is_favorite": False
            })
        
        return Response({
            "message": "Kitob yoqqanlarga qo'shildi",
            "is_favorite": True
        }, status=status.HTTP_201_CREATED)



class ClearAllFavoritesView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        Favorite.objects.filter(user=request.user).delete()
        return Response({
            "message": "Barcha yoqqan kitoblar o'chirildi"
        })