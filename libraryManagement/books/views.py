from rest_framework import generics
from .models import books, Genre
from .serializers import books_serializer, genre_serializer

# Create your views here.

class createViewBook(generics.ListCreateAPIView):
    queryset = books.objects.all()
    serializer_class = books_serializer
    
class editDeleteBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = books.objects.all()
    serializer_class = books_serializer
    
class createViewGenre(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = genre_serializer
    
class editDeleteGenre(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = genre_serializer