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

