from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def say_hello(request):
    return render(request,'hello.html')
def page1(request):
    return render(request,'page1.html')
def login(request):
    return render(request, 'login.html')
def index(request):
    return render(request, 'index.html')
@login_required
def home(request):
    return render(request, 'home.html')