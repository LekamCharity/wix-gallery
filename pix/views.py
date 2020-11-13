from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to Wix-gallery')

def home(request):
    title = "Welcome to Wix-gallery"
    images = Image.fetch_all()
    locations = Location.fetch_locations()
    categories = Category.fetch_categories() 

    context = {
        'title' : title ,
        'images' : images,
        'locations' : locations,
        'categories' : categories,
    }
    return render(request,'welcome.html',context)

def location(request,location):
    print(location)
    images = Image.get_by_location(location)
    title = location
    breadcrumb = "Location"
    
    context = {
       "images" : images , 
       "title" : title , 
       "breadcrumb" : breadcrumb, 
    }
    return render(request,'location.html', context )


