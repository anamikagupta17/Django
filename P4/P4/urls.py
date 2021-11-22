
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('course/',include('Course.urls')),
    path('fee/',include('Fee.urls')),
    path('lang/',include('Language.urls')),
]
