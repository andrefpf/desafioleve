# desafioleve
Uma API REST simples, desenvolvida em Python usando Django e Django Rest Framework, para manipular uma base de dados composta por modelos de usuário e salário. 

## Instalar
- Clone ou faça download do repositório.
- Crie um ambiente virtual (opcional)
- Na raiz do projeto execute ```pip install -r requirements.txt``` no terminal para instalar os requisitos.

## Executar o servidor de testes
- Na raiz do projeto execute o comando ```python manage.py migrate``` para preparar o banco de dados.
- Execute ```python manage.py runserver``` para iniciar o servidor.

## Executar os testes unitários
- Na raiz do projeto execute ```python manage.py test```

## Utilizar a API
Após executar o servidor é possível utilizá-la através dos seguintes endereços:

- http://localhost:8000/users/
- http://localhost:8000/salaries/
- http://localhost:8000/global/

Vale ressaltar que o modo DEBUG do Django está ativado no arquivo settings.py


### users
  Endpoint utilizado para lidar com as operações relacionadas ao usuário.
  Podem ser executados os métodos GET e POST para realizar as operações na coleção como um todo. 
  Para manipular items específicos e usar as demais operações CRUD acesse-os através do link ```.../users/{pk}```.
  
  Os dados enviados para as operações POST e PUT devem estar no formato JSON e seguir o modelo
  ```
  {
    "name" : "André Fernandes", 
    "cpf" : "12345678900", 
    "birthday" : "1822-01-01"
  }
  ```
  
### salaries
  Endpoint utilizado para lidar com as operações relacionadas aos pagamentos.
  Podem ser executados os metodos GET e POST para realizar as operações na coleção como um todo.
  Para manipular itens específicos e usar as demais operações CRUD acesse-os através do link ```.../salaries/{pk}```
  
  Os dados enviados para as operações POST e PUT devem estar no formato JSON e seguir o modelo
  ```
  {
      "date" : "2020-12-17",
      "cpf" : "12345678900",
      "salary" : "2000.00",
      "discount" : "2.00"
  }
  ```

### global
  Endpoint utilizado para informar dados gerais sobre o banco de dados, como o salário médio, média de descontos, etc.
  Apenas o método GET está disponível neste caso.


## Requerimentos
  - [Django](https://github.com/django/django)
  - [Django Rest Api](https://github.com/encode/django-rest-framework)



