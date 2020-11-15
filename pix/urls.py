from django.conf.urls import url ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url('^$',views.home,name = 'index'),
    url('^$',views.location,name = 'location'),
    url('^$',views.category,name = 'category'),
    url('^$',views.search_images,name = 'search_images'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
