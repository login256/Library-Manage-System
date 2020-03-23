from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    name = models.CharField(max_length=128, null=True)
    isbn = models.CharField(max_length=16, null=True)
    author = models.CharField(max_length=128, null=True)
    publisher = models.CharField(max_length=128, null=True)


class BookItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status_choices = [(0,'Not borrowed'), (1,'Borrowed')]
    status = models.IntegerField(choices=status_choices, default=0)


class User(AbstractUser):
    arrears = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    borrowed = models.ManyToManyField(BookItem, through='Borrow')

    class Meta(AbstractUser.Meta):
        pass


class Borrow(models.Model):
    bookitem = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_borrow = models.DateField()
    date_return = models.DateField(null=True, blank=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
