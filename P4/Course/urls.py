
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('learnDj/', views.learnDjango),
    path('learnPy/', views.learnPython),
]
