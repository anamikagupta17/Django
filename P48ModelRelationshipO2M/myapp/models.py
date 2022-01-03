from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  # one to many 
    #user=models.ForeignKey(User,on_delete=models.PROTECT)  # this will not allow to delete user untill you delete all post of that user
    #user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True) # here can delete user without deleting post it will make user null for that post
    post_title=models.CharField(max_length=70)
    post_cat=models.CharField(max_length=70)
    post_publish_date=models.DateField()
