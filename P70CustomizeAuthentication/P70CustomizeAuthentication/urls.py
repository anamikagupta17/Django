"""P70CustomizeAuthentication URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from myapp.forms import LoginFrom

#use custom views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name='myapp/login.html',authentication_form=LoginFrom),name='login'), #custom login file path by defualt it will take registration/login.html,authentication_form for form changes
    path('',TemplateView.as_view(template_name='myapp/home.html'),name='home'),
    path('dashboard/',TemplateView.as_view(template_name='myapp/dashboard.html'),name='dashboard'),
    path('logout/',auth_views.LogoutView.as_view(template_name='myapp/logout.html'),name='logout'),
    path('changepass/',auth_views.PasswordChangeView.as_view(template_name='myapp/changepass.html',success_url='/changepassdone/'),name='changepass'),#reverse url for password chaneg done
    path('changepassdone/',auth_views.PasswordChangeDoneView.as_view(template_name='myapp/changepassdone.html'),name='changepassdone'), #reverse url for password chaneg done
    
    
    
    # path('resetpass/',auth_views.PasswordResetView.as_view(template_name='myapp/resetpass.html',success_url='/resetpassdone/'),name='resetpass'),
    
    
    # path('resetpassdone/',auth_views.PasswordResetDoneView.as_view(template_name='myapp/resetpassdone.html'),name='resetpassdone'),
    
    # path('resetpassconfirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='myapp/resetpassconfirm.html',success_url='/resetcomplete/'),name='resetpassconfirm'),
    
    # path('resetcomplete',auth_views.PasswordResetCompleteView.as_view(template_name='myapp/resetcomplete.html'),name='resetcomplete'),
    
    # we can do all these thing in view by creating own view and inherit main view,LoginView,Logoutview....
    
]
