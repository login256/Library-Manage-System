from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

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

