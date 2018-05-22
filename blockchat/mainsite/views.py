from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'template.html')

def about(request):
    return HttpResponse("Hello, world. This is the about page")

def HowItWorks(request):
    return HttpResponse("Hello, world. This is the how-it-works page")