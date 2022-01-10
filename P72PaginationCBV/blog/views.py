from django.http.response import Http404
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


# Create your views here.

class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    ordering=['id']
    paginate_by=3 #per page 
    #paginate_orphans=1 #adjust last page to the prevous page if 1 record in last  if2 then need to give 2

     #handle error
    def get_context_data(self, *args,**kwargs):
        try: # if exiting or correct then
            return super(PostListView,self).get_context_data(*args,**kwargs)
        except Http404: # if incorrect value then redirect to page 1
            self.kwargs['page']=1
            return super(PostListView,self).get_context_data(*args,**kwargs)
        
    # def paginate_queryset(self,queryset,page_size):
    #     try: # if exiting or correct then
    #         return super(PostListView,self).paginate_queryset(queryset,page_size)
    #     except Http404: # if incorrect value then redirect to page 1
    #         self.kwargs['page']=1
    #         return super(PostListView,self).paginate_queryset(queryset,page_size)
        
        
# can write any of the one method for error handling        
    