from django.contrib import admin
from .models import books, Genre

# Register your models here.

admin.site.register(books)
admin.site.register(Genre)
