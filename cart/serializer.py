from rest_framework import serializers
from .models import Cart, CartItem
from books.models import Book


class CartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ['id', 'added_at']



class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'

    def get_total_items(self, obj):
        return sum(item.quantity for item in obj.items.all())

    def get_total_price(self, obj):
        return sum(item.book.price * item.quantity for item in obj.items.all())