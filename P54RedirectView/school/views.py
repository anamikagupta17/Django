from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView

# Create your views here.


class ResumeRedirectView(RedirectView):
    url='http://anamikagupta.pythonanywhere.com/'
    
    
class GeekRedirectView(RedirectView):
    pattern_name='mindex'
    parmanent=True
    query_string=True #query string will show in url by default it is false
    
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        kwargs['pk']=45    # we can set 
        return super().get_redirect_url(*args, **kwargs)
