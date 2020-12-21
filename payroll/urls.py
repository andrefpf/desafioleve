from django.urls import path, include 
from .views import UserList, PaymentList, UserDetail, PaymentDetail, GlobalList


urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('salaries/', PaymentList.as_view(), name='salaries-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-list'),
    path('salaries/<int:pk>/', PaymentDetail.as_view(), name='salaries-detail'),
    path('global/', GlobalList.as_view(), name='global-list'),
]