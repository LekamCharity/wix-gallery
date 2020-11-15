from django.conf.urls import url 
from . import views
from django.conf import Settings
from django.conf.urls.static import static

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url('^$',views.home,name = 'index'),
    url('^$',views.location,name = 'location'),
    url('^$',views.category,name = 'category'),
    url('^$',views.search_images,name = 'search_images'),
]

# if Settings.DEBUG:
#     urlpatterns+= static(Settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
