from django.urls import path
from . import views

urlpatterns = [
    path('user/',views.user,name='user'),
    path('success/',views.success,name='success'),
    path('formFields/',views.formFields,name='formFields'),
]
