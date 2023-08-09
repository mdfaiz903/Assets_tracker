from django.urls import path
from . views import loginuser,logoutuser

urlpatterns = [


    path('', loginuser, name= "login"),
    path('logout/', logoutuser, name= "logout"),
 
]