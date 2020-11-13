from django.conf.urls import url 
from . import views

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url('^$',views.home,name = 'index'),
    url('^$',views.location,name = 'location'),
    url('^$',views.category,name = 'category'),
    url('^$',views.search_images,name = 'search_images'),
]
