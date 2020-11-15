from django.shortcuts import render
from django.http import HttpResponse
from .models import Image ,Location , Category

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
    return render(request,'user_interface.html', context )

def category(request,category):
    images = Image.get_by_category(category)
    title = category
    breadcrumb = "Category"

    context = {
        "images":images ,
        "title":title , 
        "breadcrumb": breadcrumb,
    }
    return render(request,'user_interface.html', context )

def search_images(request):
    if 'images' in request.GET and request.GET['images']:
        search_term = request.GET.get("images")
        images = Image.search_image(search_term)
        # status = f"Displaying images related to {search_term} "
        status = search_term
        context = {
            "status":status , 
            "images":images ,
            "title":search_term 
        }
        return render(request , 'user_interface.html', context )
    else:
        status = "Enter an input !"
        return render(request, "user_interface.html",{"status":status})