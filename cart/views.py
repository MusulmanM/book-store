from rest_framework.generics import ListCreateAPIView

from rest_framework.permissions import IsAuthenticated

from .models import Cart, CartItem

from .serializer import (
    CartSerializer, CartItemSerializer
)

# Create your views here.



class CartapiView(ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart


class CartItemapiview(ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()


