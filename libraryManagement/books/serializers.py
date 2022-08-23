from .models import books, Genre
from rest_framework import serializers

class books_serializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = '__all__'
        
class genre_serializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
