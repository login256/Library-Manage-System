from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.utils import timezone

from .models import *
from .forms import *


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("login success!")
    else:
        return HttpResponse("login failed!")


def logout_view(request):
    logout(request)
    return HttpResponse("login success!")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', context={'form': form})


def books_index(request):
    books = Book.objects.order_by("name")
    return render(request, 'books_index.html', {'books': books})


def book_show(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    bookitems = BookItem.objects.filter(book__id=book_id)
    return render(request, 'book_show.html', {'book': book, 'bookitems': bookitems})


@login_required
def borrow_book(request):
    if request.method == 'GET':
        return HttpResponse(request.GET)
    elif request.method == 'POST':
        if request.POST['id']:
            bookitem = get_object_or_404(BookItem, id=request.POST['id'])
            if bookitem.status == 1:
                return render(request, 'borrow.html', {'errors': ['Book has been borrowed!']})
            bookitem.status = 1
            borrow = Borrow(bookitem=bookitem, user=request.user,
                            date_borrow=timezone.now(), fee=0)
            borrow.save()
            redirect('/books/')
        else:
            raise Http404('Wrong POST!')
