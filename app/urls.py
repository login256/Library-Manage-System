from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name="login.html",
                                     extra_context={}), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('books/', views.books_index, name='books_index'),
    path('books/<int:book_id>', views.book_show, name='book_show'),
    path('borrow/', views.borrow_book, name="borrow"),
    path('return/', views.return_book, name="return"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('password/change/', PasswordChangeView.as_view(template_name="change_password.html",
                                                        success_url="/myaccount/"), name='password_change'),
]
