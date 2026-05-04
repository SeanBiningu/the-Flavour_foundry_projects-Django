# urls.py imports 

from django.contrib import admin 

from django.urls import path 

from django.shortcuts import render 

# THE VIEW (The Logic) 

def home_view(request): 
 
    # This 'context' dictionary is the bridge to our HTML 
 
    context = { 
 
        'site_name': 'GymFitness', 
 
        'chef_name': 'Sean Biningu', 
 
        'headline': 'Simple Training Tips for Busy Schedules', 
 
        'recipe_count': "infinite recipe to bulk"
 
    } 
    

 
    return render(request, 'index.html', context) 
 
# THE URLS (The Map) 
urlpatterns = [ 
path('admin/', admin.site.urls), 
path('', home_view), 
] 
