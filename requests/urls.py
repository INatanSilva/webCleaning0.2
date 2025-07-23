from django.urls import path
from .views import create_request, home

urlpatterns = [
    path('', home, name='home'),
    path('api/requests', create_request, name='create_request'),
] 