from django.urls import path
from .views import home, login,menu,about,contact,register,table,date,catwise,productview,order,pro_add,forgotpass,otpcheck,newpassword,logout,edit

urlpatterns = [
    path('',login,name='login'),
    path('register/',register),
    path('home/',home,name='home'),
    path('menu/',menu,name='menu'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('table/',table,name='table'),
    path('date/',date,name='date'),
    path('cat/<str:name>/',catwise,name='catwise'),
    path('productview/<int:pk>/',productview,name='productview'),
    path('pro_add/',pro_add,name='pro_add'),
    path('order/',order,name='order'),
    path('forgotpass/',forgotpass,name='forgotpass'),
    path('otpcheck/',otpcheck,name='otpcheck'),
    path('newpassword/',newpassword,name='newpassword'),  
    path('logout',logout,name='logout'), 
    path('edit',edit,name='edit'),
                     
]
