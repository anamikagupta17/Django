from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Page,Post,Song

# Create your views here.

# if we don't want to give the name of model class so we can  at the time of creating model relation related_name='mypage' or 'allsongs' anything


def users(req):
    users=User.objects.all()
    data1=User.objects.filter(email='anamika@gmail.com')
    data2=User.objects.filter(page__page_cat='Programming') #model__column_name BCZ user don't have page category
    data3=User.objects.filter(post__post_publish_date='2022-01-24') 
    data4=User.objects.filter(song__song_duration=3)
    return render(req,'users.html',{'users':users,'data1':data1,'data2':data2,'data3':data3,'data4':data4})

def home(req):
    return render(req,'home.html')

def pages(req):
    pages=Page.objects.all()
    data1=Page.objects.filter(page_cat='Programming')
    data2=Page.objects.filter(user__email='anamika@gmail.com') 
    return render(req,'page.html',{'pages':pages,'data1':data1,'data2':data2})

def posts(req):
    posts=Post.objects.all()
    data1=Post.objects.filter(post_publish_date='2022-01-24') 
    data2=Post.objects.filter(user__username='anamika')#model__column_name BCZ post don't have user table and it will filter data for post table only
    return render(req,'post.html',{'posts':posts,'data1':data1,'data2':data2})

def songs(req):
    songs=Song.objects.all()
    data1=Song.objects.filter(song_duration=3) #model__column_name BCZ user don't have page category
    data2=Song.objects.filter(user__username='roli')
    return render(req,'song.html',{'songs':songs,'data1':data1,'data2':data2})

