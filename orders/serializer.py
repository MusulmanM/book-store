from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Order
from cart.models import Cart
from users.serializer import UserSerializer

class OrderSerializer(ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'order_date']

    def validate_cart(self, value):
        if value.items.count() == 0:
            raise ValidationError("Savatcha bo'sh")
        return value
    


    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

