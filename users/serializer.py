from rest_framework.serializers import ModelSerializer
from users.models import User, Favorite


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'





class FavoriteSerializer(ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'







