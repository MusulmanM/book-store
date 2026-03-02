from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .models import User, Favorite
from users.serializer import UserSerializer, FavoriteSerializer
from rest_framework.permissions import IsAuthenticated

   

# Create your views here.




class Userapiview(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    




class Favoriteapiview(ListCreateAPIView):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
    permission_classes = [IsAuthenticated]


    def create(self, request):
        
        request.data['user'] = request.user.id
        data = super().create(request)
        print("fevourite qoshildi. ")
        print(request.user)

        return data
    


    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)