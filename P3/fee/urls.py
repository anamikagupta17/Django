from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('feepy/', views.fee_python),
   path('feeDj/', views.fee_django),
]
