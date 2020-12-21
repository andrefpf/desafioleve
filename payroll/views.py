from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .models import User, Payment
from .serializers import UserSerializer, PaymentSerializer


def get_filters(request, *fields):
    ''' Returns a dictionary that maps the desired field
    to the users input on that field.

    Args:
        request (Requests) : Http request.
        *fields (str) : Fields desired to make a filter.
    
    Returns:
        dict : Dictionary to be user on filter functions.
    '''
    
    get = request.query_params.get
    return {field : get(field) for field in fields if get(field)}


class UserList(ListCreateAPIView):
    ''' Class that creates the methods POST and GET of the entire 
    collection for the endpoint /users.
    '''

    serializer_class = UserSerializer

    def get_queryset(self):
        filters = get_filters(self.request, 'name', 'cpf', 'birthday', 
                             'average_salary', 'average_discounts',
                             'bigger_salary', 'smaller_salary')
        queryset = User.objects.all()
        if filters:
            queryset = queryset.filter(**filters)
        return queryset


class UserDetail(RetrieveUpdateDestroyAPIView):
    ''' Class that creates the methods POST, GET, PUT, PATCH and DELETE for specific
    items of the enpoint /users.
    '''
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def object_exists(self, pk):
        return Payment.objects.filter(pk=pk).exists()
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if self.object_exists:
            return Response(status=status.HTTP_409_CONFLICT)
        else:
            serializer.save(pk=pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class PaymentList(ListCreateAPIView):
    ''' Class that creates the methods POST and GET of the entire 
    collection for the endpoint /salaries.
    '''

    serializer_class = PaymentSerializer
        
    def get_queryset(self):
        filters = get_filters(self.request, 'date', 'cpf', 'salary', 'discount')
        queryset = Payment.objects.all()
        if filters:
            queryset = queryset.filter(**filters)
        return queryset


class PaymentDetail(RetrieveUpdateDestroyAPIView):
    ''' Class that creates the methods POST, GET, PUT, PATCH and DELETE for specific
    items of the enpoint /users.
    '''

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def object_exists(self, pk):
        return Payment.objects.filter(pk=pk).exists()
    
    def post(self, request, pk, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if self.object_exists:
            return Response(status=status.HTTP_409_CONFLICT)
        else:
            serializer.save(pk=pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class GlobalList(APIView):
    ''' Class that creates the GET method for the endpoint /global.'''

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
