from django.db import models

# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class books(models.Model):
    isbn = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, max_length=100, on_delete=models.CASCADE, related_name='pGenre')
    created_on = models.DateField(auto_now_add=True)
    borrowed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name