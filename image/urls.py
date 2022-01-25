

from django.urls import path
from .views import HomePageView,add,thanks

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('<int:id>/', thanks, name='thanks'),
    path('add/', add, name='add'),
]