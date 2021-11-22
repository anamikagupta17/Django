
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('feeDj/', views.feeDjango),
    path('feePy/', views.feePython),
]
