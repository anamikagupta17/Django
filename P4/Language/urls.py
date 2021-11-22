
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('langOne/', views.languageOne),
    path('langTwo/', views.languageTwo),
]
