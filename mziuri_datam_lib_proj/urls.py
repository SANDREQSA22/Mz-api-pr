from django.contrib import admin
from django.urls import path, include
from library.api import api 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls')), 
    path('api/', api.urls),  
]
