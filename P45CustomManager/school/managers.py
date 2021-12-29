from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name') # get base class function and set order by
    # custom method
    
    def get_stu_roll_range(self,r1,r2):
        return super().get_queryset().filter(roll__range=(r1,r2)).order_by('name')
    
    


    