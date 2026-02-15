from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Favorite
from books.models import Book



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'



    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Parollar mos emas")
        return data



    def create(self, validated_data):
        validated_data.pop('password2')
        
        validated_data['username'] = validated_data['email'].split('@')[0]
        
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        
        if not user:
            raise serializers.ValidationError("Email yoki parol xato")
        
        if not user.is_active:
            raise serializers.ValidationError("Foydalanuvchi faol emas")
        
        return {'user': user}
    





class FavoriteSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    book_title = serializers.CharField(source='book.title', read_only=True)
    
    class Meta:
        model = Favorite
        fields = '__all__'
        read_only_fields = ['id', 'added_at']

class FavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = 'book'

    def validate_book(self, value):
        user = self.context['request'].user
        if Favorite.objects.filter(user=user, book=value).exists():
            raise serializers.ValidationError("Bu kitob allaqachon yoqqanlar ro'yxatida")
        return value

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class FavoriteListSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()  
    
    class Meta:
        model = Favorite
        fields = '__all__'