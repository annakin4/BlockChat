from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('how-it-works/', views.HowItWorks, name='How It works'),
]