from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from books.models import Book
from .serializer import (
    CartSerializer, 
    CartItemSerializer, 
    CartItemCreateSerializer,
    CartItemUpdateSerializer
)

# Create your views here.



class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart


class CartItemCreateView(generics.CreateAPIView):
    serializer_class = CartItemCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)


class CartItemUpdateView(generics.UpdateAPIView):
    serializer_class = CartItemUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)


class CartItemDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)


class CartClearView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        cart.items.all().delete()
        return Response({"message": "Savatcha tozalandi"})


class CartItemQuantityView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, item_id, action):
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        
        if action == 'increase':
            if cart_item.book.stock > cart_item.quantity:
                cart_item.quantity += 1
                cart_item.save()
                return Response({"message": "Miqdor oshirildi", "quantity": cart_item.quantity})
            return Response({"error": "Omborda yetarli kitob yo'q"}, status=400)
        
        elif action == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                return Response({"message": "Miqdor kamaytirildi", "quantity": cart_item.quantity})
            else:
                cart_item.delete()
                return Response({"message": "Kitob savatchadan o'chirildi"})
        
        return Response({"error": "Noto'g'ri amal"}, status=400)