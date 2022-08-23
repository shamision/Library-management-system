from .views import createViewBorrowedBook, editDeleteBorrowedBook
from django.urls import path

urlpatterns = [
    path('borrowedBooks', createViewBorrowedBook.as_view()),
    path('editBorrowedBooks', editDeleteBorrowedBook.as_view()),
]
