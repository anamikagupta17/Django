from django.db import models
from django.contrib.auth.models import User # auth user

# Create your models here.

# we can create our own User model

class Page(models.Model):
    #user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True) #cascade mens if user delete then page also deleted and this will be foriegn key of user model class so we can given this as primary key
    
    #user=models.OneToOneField(User, on_delete=models.PROTECT,primary_key=True) # user can not be deleted if has page
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,limit_choices_to={'is_staff':True}) # in this case only staff can add the page 
   
    page_name=models.CharField(max_length=70)
    page_cat=models.CharField(max_length=70)
    page_publish_date=models.DateField()
    