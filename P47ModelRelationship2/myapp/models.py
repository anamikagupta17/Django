from django.db import models
from django.contrib.auth.models import User # auth user

# Create your models here.

# we can create our own User model

class Page(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True) # in this case only staff can add the page 
    page_name=models.CharField(max_length=70)
    page_cat=models.CharField(max_length=70)
    page_publish_date=models.DateField()
    
    
class Like(Page):
    # this will also create one to one relationship with user because we are inheriting this with baseapp
     
    # if we don't want it    O2O relationship then we need to define
    
    pageid=models.OneToOneField(Page, on_delete=models.CASCADE,primary_key=True,parent_link=True) #by default parent_link will be False
    likes=models.IntegerField()  
    