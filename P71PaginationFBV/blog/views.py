from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

def post_list(req):
    all_post=Post.objects.all()
    paginator=Paginator(all_post,3,orphans=1) # object, 3 means per page 3 #orphans if we want to adjus last page data into second last if its 1 then 1 if its 2 then orphans=2 its optional
    print("Paginator",paginator)
    page_number=req.GET.get('page') #page number
    page_object=paginator.get_page(page_number) #posts according to page  1st page 2ndpage...
    print("Page Object",page_object)
    return render(req,'blog/home.html',{'posts':page_object})
