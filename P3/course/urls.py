from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('learnpy/', views.learn_python),
   path('learnDj/', views.learn_django),
]
