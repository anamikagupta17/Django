from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@login_required # when login then only can see profile
def profile(req):
    return render(req,'registration/profile.html')


@staff_member_required # only staff can access this page
def about(req):
    return render(req,'registration/about.html')
