from rest_framework import serializers
from .models import Cart, CartItem
from books.models import Book


class CartItemSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    book_price = serializers.DecimalField(source='book.price', read_only=True, max_digits=10, decimal_places=2)

    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ['id', 'added_at']

# CartItem qo'shish uchun serializer
class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

    def validate(self, data):
        book = data['book']
        if book.stock < data['quantity']:
            raise serializers.ValidationError(f"Omborda faqat {book.stock} dona bor")
        return data


class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    total_items = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = '__all__'

    def get_total_items(self, obj):
        return sum(item.quantity for item in obj.items.all())

    def get_total_price(self, obj):
        return sum(item.book.price * item.quantity for item in obj.items.all())