from rest_framework import serializers
from .models import Order
from cart.models import Cart
from users.serializer import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'order_date']

    def validate_cart(self, value):
        
        if value.items.count() == 0:
            raise serializers.ValidationError("Savatcha bo'sh")
        return value

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'