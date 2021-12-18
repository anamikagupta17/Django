from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed

from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in,sender=User)  #2
def login_success(sender,request,user,**kwargs):  #receiver function
    print('------------------------------')
    print('Logged In Signal.......') #can write any intro here
    print('Sender :',sender)
    print('Request :',request)
    print('User :',user)
    print('User Password :',user.password)
    print('User username :',user.username)
    print(f'Kwargs : {kwargs}')
    
    
#user_logged_in.connect(login_success,sender=User) # 1 User is sender,user_logged_in is signal,connect is a method

@receiver(user_logged_out,sender=User)
def logout_success(sender,request,user,**kwargs):
    print('------------------------------')
    print('Logged Out Signal....... Bye') 
    print('Sender :',sender)
    print('Request :',request)
    print('User :',user)
    print(f'Kwargs : {kwargs}')
    

@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):  
    print('------------------------------')
    print('Logged In Failed.......') 
    print('Sender :',sender)
    print('Request :',request)
    print('User :',credentials)
    print(f'Kwargs : {kwargs}')
    
 