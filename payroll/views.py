from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Payment
from .serializers import UserSerializer, PaymentSerializer


def get_filters(view, *fields):
    ''' Returns a dictionary that maps the desired field
    to the users input on that field.

    Args:
        view (ListCreateAPIView) : Django Class.
        *fields (str) : Fields desired to make a filter.
    
    Returns:
        dict : Dictionary to be user on filter functions.
    '''
    
    get = view.request.query_params.get
    return {field : get(field) for field in args if get(field)}


class UserList(ListCreateAPIView):
    ''' Class that set and filter the json output of the API for the endpoint /users.'''

    serializer_class = UserSerializer

    def get_queryset(self):
        filters = get_filters(self, 'name', 'cpf', 'birthday', 
                                    'average_salary', 'average_discounts',
                                    'bigger_salary', 'smaller_salary')
        queryset = User.objects.all()
        if filters:
            queryset = queryset.filter(**filters)
        return queryset


class PaymentList(ListCreateAPIView):
    ''' Class that set and filter the json output of the API for the endpoint /salaries.'''

    serializer_class = PaymentSerializer

    def get_queryset(self):
        filters = get_filters(self, 'date', 'cpf', 'salary', 'discount')
        queryset = Payment.objects.all()
        if filters:
            queryset = queryset.filter(**filters)
        return queryset


class GlobalList(APIView):
    ''' Class that set the json output of the API for the endpoint /global.'''

    def get(self, request):
        average = lambda x: sum(x) / len(x)
        queryset = Payment.objects.all()
        salaries = [i['salary'] for i in queryset.values()]
        discounts = [i['discount'] for i in queryset.values()]

        average_salary = average(salaries) if salaries else 0
        average_discount = average(discounts) if salaries else 0
        bigger_salary = max(salaries) if salaries else 0
        smaller_salary = min(salaries) if salaries else 0
        
        data = {
            'average_salary' : round(average_salary, 2),
            'average_discount' : round(average_discount, 2),
            'bigger_salary' : round(bigger_salary, 2),
            'smaller_salary' : round(smaller_salary, 2),
        }

        return Response(data)
