from django.urls import path, include 
from .views import UserList, PaymentList, GlobalList


urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('salaries/', PaymentList.as_view(), name='salaries-list'),
    path('global/', GlobalList.as_view(), name='global-list')
]