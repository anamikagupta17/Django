from django.urls import path
from . import views

urlpatterns = [
    path('registration/',views.showFormData,name='registration'),
    path('errors/',views.errors,name='errors')
]
