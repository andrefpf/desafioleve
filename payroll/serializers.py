from rest_framework import serializers
from .models import User, Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'cpf', 'birthday', 'average_salary', 
                  'average_discounts', 'bigger_salary', 'smaller_salary')
    
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('date', 'cpf', 'salary', 'discount')