from rest_framework import serializers
from .models import User, Payment


class UserSerializer(serializers.ModelSerializer):
    ''' Class to serialize the User database model into some 
    default web format like JSON.
    '''

    class Meta:
        model = User
        fields = ('pk', 'name', 'cpf', 'birthday', 'average_salary', 
                  'average_discounts', 'bigger_salary', 'smaller_salary')
    
class PaymentSerializer(serializers.ModelSerializer):
    ''' Class to serialize the Payment database model into some 
    default web format like JSON.
    '''

    class Meta:
        model = Payment
        fields = ('pk', 'date', 'cpf', 'salary', 'discount')