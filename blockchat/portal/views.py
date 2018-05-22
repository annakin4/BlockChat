from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return HttpResponse("Hello, world. This is the login page")

def dashboard(request):
    return HttpResponse("Hello, world. This is the dashboard page")

def addressBook(request):
    return HttpResponse("Hello, world. This is the address book page")