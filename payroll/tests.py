from django.test import TestCase
from rest_framework.test import RequestsClient

from .views import UserList, UserDetail, PaymentList, PaymentDetail, GlobalList

from collections import OrderedDict


class ExampleTest(TestCase):

    def setUp(self):
        self.client = RequestsClient()

    def test_example(self):
        INPUT_USERS = [ 
            {
                'name' : 'João da Silva', 
                'cpf' : '12345678900', 
                'birthday' : '1980-08-05',
            },
            {
                'name' : 'Luke Skywalker', 
                'cpf' : '12345678901', 
                'birthday' : '1975-05-10',
            },
        ]

        INPUT_SALARIES = [
            {
                'date' : '2020-12-17',
                'cpf' : '12345678900',
                'salary' : '2000.00',
                'discount' : '2.00',
            },

            {
                'date' : '2020-12-17',
                'cpf' : '12345678900',
                'salary' : '5000.00',
                'discount' : '4.00',
            },

            {
                'date' : '2020-12-17',
                'cpf' : '12345678901',
                'salary' : '500.00',
                'discount' : '4.00',
            },

            {
                'date' : '2020-12-17',
                'cpf' : '12345678901',
                'salary' : '300.00',
                'discount' : '8.00',
            },

            {
                'date' : '2020-12-17',
                'cpf' : '12345678901',
                'salary' : '45678.00',
                'discount' : '22.71',
            },
        ]

        EXPECTED_USERS_OUTPUT = [
            {   
                'pk' : 1,
                'name' : 'João da Silva Sauro', 
                'cpf' : '12345678900', 
                'birthday' : '1980-08-05',
                'average_salary' : 3000.00,
                'average_discounts' : 3.00,
                'bigger_salary' : 4000,
                'smaller_salary' : 2000,
            },
            {
                'pk' : 2,
                'name' : 'Luke Skywalker', 
                'cpf' : '12345678901', 
                'birthday' : '1975-05-10',
                'average_salary' : 400.00,
                'average_discounts' : 6.00,
                'bigger_salary' : 500,
                'smaller_salary' : 300,
            },
        ]

        EXPECTED_SALARIES_OUTPUT = [
            {
                'pk' : 1,
                'date' : '2020-12-17',
                'cpf' : '12345678900',
                'salary' : '2000.00',
                'discount' : '2.00',
            },

            {
                'pk' : 2,
                'date' : '2020-12-17',
                'cpf' : '12345678900',
                'salary' : '4000.00',
                'discount' : '4.00',
            },

            {   
                'pk' : 3,
                'date' : '2020-12-17',
                'cpf' : '12345678901',
                'salary' : '500.00',
                'discount' : '4.00',
            },

            {
                'pk' : 4,
                'date' : '2020-12-17',
                'cpf' : '12345678901',
                'salary' : '300.00',
                'discount' : '8.00',
            },
        ]

        EXPECTED_GLOBAL_OUTPUT = {
            'average_salary' : 1700.00,
            'average_discount' : 4.50,
            'bigger_salary' : 4000.00,
            'smaller_salary' : 300,
        }

        URL = 'http://testserver/'


        for data in INPUT_USERS:
            self.client.post(URL + 'users/', data)

        for data in INPUT_SALARIES:
            self.client.post(URL + 'salaries/', data)

        self.client.patch(URL + 'users/1/', {'name':'João da Silva Sauro'})
        self.client.patch(URL + 'salaries/2/', {'salary' : '4000.00'})
        self.client.delete(URL + 'salaries/5/')

        response = self.client.get(URL + 'users/')
        assert response.json() == EXPECTED_USERS_OUTPUT

        response = self.client.get(URL + 'salaries/')
        assert response.json() == EXPECTED_SALARIES_OUTPUT

        response = self.client.get(URL + 'global/')
        assert response.json() == EXPECTED_GLOBAL_OUTPUT


class GlobalTest(TestCase):

    def setUp(self):
        self.client = RequestsClient()

    def test_user(self):
        INPUT_DATA = [ 
            {
                'name':'João da Silva', 
                'cpf':'12345678900', 
                'birthday':'1980-08-05',
            },
            {
                'name':'Luke Skywalker', 
                'cpf':'12345678901', 
                'birthday':'1975-05-10',
            },
        ]

        EXPECTED_OUTPUT = [
            {
                'pk':1,
                'name':'João da Silva',
                'cpf':'12345678900',
                'birthday':'1980-08-05',
                'average_salary':0,
                'average_discounts':0,
                'bigger_salary':0,
                'smaller_salary':0,
            },
            {
                'pk':2,
                'name':'Luke Skywalker',
                'cpf':'12345678901',
                'birthday':'1975-05-10',
                'average_salary':0,
                'average_discounts':0,
                'bigger_salary':0,
                'smaller_salary':0,
            },
        ]

        URL = 'http://testserver/'

        for data in INPUT_DATA:
            self.client.post(URL + 'users/', data)

        response = self.client.get(URL + 'users/')
        assert response.json() == EXPECTED_OUTPUT

    def test_salary(self):
        INPUT_DATA = [
            {
                'date' : '2020-12-17',
                'cpf' : '12345678900',
                'salary' : '2000.00',
                'discount' : '2.00',
            },
            {
                'date' : '2020-12-17',
                'cpf' : '12345678908',
                'salary' : '509.00',
                'discount' : '4.00',
            },
        ]

        EXPECTED_OUTPUT = [
            {
                'pk' : 1,
                'date' : '2020-12-17',
                'cpf' : '12345678900',
                'salary' : '2000.00',
                'discount' : '2.00',
            },
            {   
                'pk' : 2,
                'date' : '2020-12-17',
                'cpf' : '12345678908',
                'salary' : '509.00',
                'discount' : '4.00',
            },
        ]

        URL = 'http://testserver/'

        for data in INPUT_DATA:
            self.client.post(URL + 'salaries/', data)

        response = self.client.get(URL + 'salaries/')
        assert response.json() == EXPECTED_OUTPUT

    def test_global(self):
        EXPECTED_OUTPUT = {
            'average_salary' : 0,
            'average_discount' : 0,
            'bigger_salary' : 0,
            'smaller_salary' : 0
        }

        URL = 'http://testserver/'

        response = self.client.get(URL + 'global/')
        assert response.json() == EXPECTED_OUTPUT


class CRUDTests(TestCase):
    def setUp(self):
        self.client = RequestsClient()
    
    def test_user(self):
        INPUT_DATA = [ 
            {
                'name':'André Fernandes', 
                'cpf':'12345678902', 
                'birthday':'2000-01-01'
            },
            {
                'name':'João da Silva', 
                'cpf':'12345678900', 
                'birthday':'1980-08-05'
            },
            {
                'name':'Luke Skywalker', 
                'cpf':'12345678901', 
                'birthday':'1975-05-10',
            },
        ]

        PATCH_DATA = {'name':'João da Silva Sauro'}
        
        PUT_DATA = {
            'name':'Lucas Andarilho do Céu', 
            'cpf':'12345678910', 
            'birthday':'1976-06-11',
        }

        EXPECTED_OUTPUT = [
            {
                'pk':1,
                'name':'João da Silva Sauro',
                'cpf':'12345678900',
                'birthday':'1980-08-05',
                'average_salary':0,
                'average_discounts':0,
                'bigger_salary':0,
                'smaller_salary':0,
            },
            {
                'pk':2,
                'name':'Lucas Andarilho do Céu',
                'cpf':'12345678910',
                'birthday':'1976-06-11',
                'average_salary':0,
                'average_discounts':0,
                'bigger_salary':0,
                'smaller_salary':0,
            },
        ]

        URL = 'http://testserver/'

        for i, data in enumerate(INPUT_DATA):
            self.client.post(URL + f'users/{i}/', data)

        self.client.patch(URL + 'users/1/', PATCH_DATA)
        self.client.put(URL + 'users/2/', PUT_DATA)
        self.client.delete(URL + 'users/0/')

        response = self.client.get(URL + 'users/1/')
        assert response.json() == EXPECTED_OUTPUT[0]

        response = self.client.get(URL + 'users/2/')
        assert response.json() == EXPECTED_OUTPUT[1]

        response = self.client.post(URL + 'users/1/', INPUT_DATA[0])
        assert response.status_code == 409

        response = self.client.get(URL + 'users/0/')
        assert response.status_code == 404

    def test_salary(self):
        INPUT_DATA = [
            {
                'date' : '2020-12-17',
                'cpf' : '12345678900',
                'salary' : '2000.00',
                'discount' : '2.00',
            },
            {
                'date' : '2019-11-01',
                'cpf' : '12345678908',
                'salary' : '509.00',
                'discount' : '4.00',
            },
            {
                'date' : '2020-12-17',
                'cpf' : '98765432100',
                'salary' : '98000.00',
                'discount' : '1.00',
            },
        ]

        PATCH_DATA = {'date':'2020-09-16'}
        
        PUT_DATA = {
            'date' : '2012-11-01',
            'cpf' : '12345678988',
            'salary' : '220.00',
            'discount' : '3.00',
        }

        EXPECTED_OUTPUT = [
            {
                'pk' : 0,
                'date' : '2020-09-16',
                'cpf' : '12345678900',
                'salary' : '2000.00',
                'discount' : '2.00',
            },
            {   
                'pk' : 2,
                'date' : '2012-11-01',
                'cpf' : '12345678988',
                'salary' : '220.00',
                'discount' : '3.00',
            },
        ]

        URL = 'http://testserver/'

        for i, data in enumerate(INPUT_DATA):
            self.client.post(URL + f'salaries/{i}/', data)

        self.client.patch(URL + 'salaries/0/', PATCH_DATA)
        self.client.put(URL + 'salaries/2/', PUT_DATA)
        self.client.delete(URL + 'salaries/1/')

        response = self.client.get(URL + 'salaries/0/')
        assert response.json() == EXPECTED_OUTPUT[0]

        response = self.client.get(URL + 'salaries/2/')
        assert response.json() == EXPECTED_OUTPUT[1]

        response = self.client.post(URL + 'salaries/0/', INPUT_DATA[0])
        assert response.status_code == 409

        response = self.client.get(URL + 'salaries/1/')
        assert response.status_code == 404
