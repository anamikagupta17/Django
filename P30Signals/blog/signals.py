from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_delete,post_save,post_init,pre_migrate,post_migrate
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.backends.signals import connection_created

#User will be your user  model

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
    
    
#user_logged_in.connect(login_success,sender=User) # 1 User is sender,user_logged_in is signal,connect is a method to connect

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
    
    
#signal using built in function modals

@receiver(pre_save,sender=User)
def at_begining_save(sender,instance,**kwargs): #it will run in the begining of save
    print('------------------------------')
    print('Pre Save Signal.......') 
    print('Sender :',sender)
    print('Instance :',instance)
    print(f'Kwargs : {kwargs}')    
    
    
    
@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs): #it will run at the end of save
    if created: # True when new record
        print('------------------------------------------')
        print('Post Save Signal') 
        print('New Record.......') 
        print('Sender :',sender)
        print('Instance :',instance)
        print('Created :',created)
        print(f'Kwargs : {kwargs}')        
    else:
        print('------------------------------------------')
        print('Post Save Signal') 
        print('Updated Record.......') 
        print('Sender :',sender)
        print('Instance :',instance)
        print('Created :',created)
        print(f'Kwargs : {kwargs}')  
        
@receiver(pre_delete,sender=User)        
def at_beginig_delete(sender,instance,**kwargs):
    print('------------------------------')
    print('Pre Delete Signal.......') 
    print('Sender :',sender)
    print('Instance :',instance)
    print(f'Kwargs : {kwargs}')            
        
        
@receiver(post_delete,sender=User)        
def at_ending_delete(sender,instance,**kwargs):
    print('------------------------------')
    print('Post Delete Signal.......') 
    print('Sender :',sender)
    print('Instance :',instance)
    print(f'Kwargs : {kwargs}')           
 
 #init siganls run at the instance(when you save code it will run and also when you run server)
 
@receiver(pre_init,sender=User)        
def pre_init_siganl(sender,*args,**kwargs):
    print('------------------------------')
    print('Pre Init Signal.......') 
    print('Sender :',sender)
    print('Args :',args)
    print(f'Kwargs : {kwargs}')            
        
        
@receiver(post_init,sender=User)        
def post_init_siganl(sender,*args,**kwargs):
    print('------------------------------')
    print('Post Init Signal.......') 
    print('Sender :',sender)
    print('Args :',args)
    print(f'Kwargs : {kwargs}')           
  
  
  
 # on the request 
 
@receiver(request_started)        
def at_beginig_request(sender,environ,**kwargs):
    print('------------------------------')
    print('At the Begining Request.......') 
    print('Sender :',sender)
    print('Environ :',environ)
    print(f'Kwargs : {kwargs}')            
        
        
@receiver(request_finished)        
def at_ending_request(sender,**kwargs):
    print('------------------------------')
    print('At the Ending Request......') 
    print('Sender :',sender)
    print(f'Kwargs : {kwargs}')  
    
@receiver(got_request_exception)        
def at_req_exception(sender,request,**kwargs):
    print('------------------------------')
    print('Request Exception.......') 
    print('Sender :',sender)
    print('Request :',request)
    print(f'Kwargs : {kwargs}')   
    
    
#after migrate and flush
    
@receiver(pre_migrate)        
def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print('------------------------------')
    print('Pre Migrate Signal.......') 
    print('Before Install App.......') 
    print('Sender :',sender)
    print('App_config :',app_config)
    print('verbosity :',verbosity)
    print('interactive :',interactive)
    print('using :',using)
    print('plan :',plan)
    print('apps :',apps)
    print(f'Kwargs : {kwargs}')            
        
        
@receiver(post_migrate)        
def after_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print('------------------------------')
    print('Post Migrate Signal.......') 
    print('Sender :',sender)
    print('verbosity :',app_config)
    print('verbosity :',verbosity)
    print('interactive :',interactive)
    print('using :',using)
    print('plan :',plan)
    print('apps :',apps)
    print(f'Kwargs : {kwargs}')          
    
    
# when database connection initiated    

@receiver(connection_created)        
def connection_db(sender,connection,**kwargs):
    print('------------------------------')
    print('Initial Connection to the database.......') 
    print('Sender :',sender)
    print('Connection :',connection)
    print(f'Kwargs : {kwargs}')   