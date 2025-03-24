from django.contrib import admin
from django.urls import path, include
from api.urls import api

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', api.urls),  
]