from rest_framework.serializers import ModelSerializer
from .models import Author




class  AuthorSerializer(ModelSerializer):
    
    class Meta:
        fields='all'
        model=Author