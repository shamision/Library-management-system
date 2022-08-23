from .models import borrow_book
from .serializers import borrowSerializer
from rest_framework import generics

# Create your views here.
class createViewBorrowedBook(generics.ListCreateAPIView):
    queryset = borrow_book.objects.all()
    serializer_class = borrowSerializer
    
class editDeleteBorrowedBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = borrow_book.objects.all()
    serializer_class = borrowSerializer