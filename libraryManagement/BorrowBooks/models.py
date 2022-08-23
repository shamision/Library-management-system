from django.db import models
from account.models import User
from books.models import books
from datetime import datetime, timedelta
# Create your models here.

def expiring_date():
    return datetime.today() + timedelta(days=30)

class borrow_book(models.Model):
    borrower = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE)
    book = models.ForeignKey(books, max_length=100, on_delete=models.CASCADE)
    borrowed = models.BooleanField(default=False)
    borrowed_on = models.DateField(auto_now_add=True)
    retrieve_on = models.DateField(default=expiring_date)
    fine = models.BooleanField(default=False)
    
    
    

    