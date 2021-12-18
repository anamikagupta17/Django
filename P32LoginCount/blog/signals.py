from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache

@receiver(user_logged_in,sender=User)
def login_suucess(sender,request,user,**kwargs):
    print('----------------------------------------------')
    print('Logged in Signal ......Run Intro')
    ip=request.META.get('REMOTE_ADDR') #get IP address
    request.session['ip']=ip
    ct=cache.get('count',0,version=user.pk) # here used version because it will cache separatly for different-2 user
    newcount=ct+1
    cache.set('count',newcount,50,version=user.pk) #pk is generate different for every user
    
    
    
    
    
    
    