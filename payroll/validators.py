import re
from django.core.exceptions import ValidationError

def cpf_validator(value):
    cpf = re.sub('[^0-9]', '', value)
    if len(cpf) != 11:
        raise ValidationError('CPF must have 11 digits.', code='invalid')