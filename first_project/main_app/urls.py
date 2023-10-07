 
from django.urls import path
from .views import *

urlpatterns = [
    path('gg',index,name='index_page'),
    path('regitrations',Registration,name='registration'),
    path('user_login',user_login,name='user'),
]