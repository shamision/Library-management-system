from django.urls import path
from .views import createViewBook, editDeleteBook, createViewGenre,editDeleteGenre

urlpatterns = [
    path('createBook/', createViewBook.as_view()),
    path('updateBook/<int:pk>/', editDeleteBook.as_view()),
    path('createGenre/', createViewGenre.as_view()),
    path('updateGenre/<int:pk>/', editDeleteGenre.as_view()),
]