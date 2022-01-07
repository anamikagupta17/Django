"""P54RedirectView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import Pattern
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.TemplateView.as_view(template_name='home.html'),name='base'),
    path('home/',views.RedirectView.as_view(url='/'),name='home'),#will redirect to base
    path('index/',views.RedirectView.as_view(url='/'),name='index'),
    path('anamika/',views.RedirectView.as_view(url='http://anamikagupta.pythonanywhere.com/'),name='anamika'), #for external url
    path('resume/',views.ResumeRedirectView.as_view(),name='resume'),
    path('pattern/',views.RedirectView.as_view(pattern_name='home'),name='pattern'),#this wil go to the home url and then base url(becuse  home url redirect to  base)
    path('<int:pk>/',views.TemplateView.as_view(template_name='home.html'),name='mindex'),
    path('home/<int:pk>/',views.GeekRedirectView.as_view(),name='geek'), #this will redirect to  mindex url with the value
]
