from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in,sender=User)
def login_suucess(sender,request,user,**kwargs):
    print('----------------------------------------------')
    print('Logged in Signal ......Run Intro')
    ip=request.META.get('REMOTE_ADDR') #get IP address
    request.session['ip']=ip
    print('IP : ',ip)