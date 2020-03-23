from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html", extra_context={}), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('books/', views.books_index, name = 'books_index'),
    path('books/<int:book_id>', views.book_show, name = 'book_show'),
    path('borrow/', views.borrow_book, name = "borrow")
]