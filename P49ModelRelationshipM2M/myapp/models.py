from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Song(models.Model):
    user=models.ManyToManyField(User) #multiple user can create one song or vice versa
    song_name=models.CharField(max_length=70)
    song_duration=models.IntegerField()



    def written_by(self):
        return ",".join([str(p) for p in self.user.all()])  #comperhansion