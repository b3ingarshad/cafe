from django.urls import path
from .views import oddeven

urlpatterns = [
    path('',oddeven)
    
]