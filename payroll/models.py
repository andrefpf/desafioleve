from django.db.models import Model, CharField, DateField, DecimalField
from django.core.validators import RegexValidator
from random import randint

from .validators import cpf_validator


class CPFField(CharField):
    default_validators = [RegexValidator(r'\d{11}', 'CPF must have 11 numerical digits, without dots or dashes.')]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 11)
        super().__init__(*args, **kwargs)


class User(Model):
    class Meta:
        db_table = 'user'

    name = CharField(max_length=200)
    cpf = CPFField(unique=True)
    birthday = DateField()

    def average_salary(self):
        average = lambda x: sum(x) / len(x)
        queryset = Payment.objects.filter(cpf=self.cpf)
        salaries = [i['salary'] for i in queryset.values()]
        response = average(salaries) if salaries else 0
        return round(response, 2)

    def average_discounts(self):
        average = lambda x: sum(x) / len(x)
        queryset = Payment.objects.filter(cpf=self.cpf)
        discounts = [i['discount'] for i in queryset.values()]
        response = average(discounts) if discounts else 0
        return round(response, 2)

    def bigger_salary(self):
        queryset = Payment.objects.filter(cpf=self.cpf)
        salaries = [i['salary'] for i in queryset.values()]
        response = max(salaries) if salaries else 0
        return round(response, 2)

    def smaller_salary(self):
        queryset = Payment.objects.filter(cpf=self.cpf)
        salaries = [i['salary'] for i in queryset.values()]
        response = min(salaries) if salaries else 0
        return round(response, 2)


class Payment(Model):
    class Meta:
        db_table = 'salary'
    
    date = DateField()
    cpf = CPFField()
    salary = DecimalField(max_digits=10, decimal_places=2)
    discount = DecimalField(max_digits=10, decimal_places=2)
