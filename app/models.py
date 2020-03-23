from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    name = models.DateField(max_length = 100)
    isbn = models.DateField(max_length = 20)
    author = models.DateField(max_length = 100)
    publisher = models.DateField(max_length = 100)
    
class BookItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.TextChoices('Not borrowed', 'Borrowed')

class Borrow(models.Model):
    bookitem = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)