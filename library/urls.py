from django.urls import path
from django.http import JsonResponse
from .api import api

def home(request):
    return JsonResponse({"message": "Library Management System API"})

urlpatterns = [
    path('', home),  
    path('api/', api.urls), 
]
