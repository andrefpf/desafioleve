import re
from django.core.exceptions import ValidationError

def cpf_validator(value):
    ''' Function to check if it is a valid CPF.

    Actually it should complain about other things, like the 
    verification digit. But it isn't necessary in this context.

    Args:
        value (str) : User CPF
        
    '''
    
    cpf = re.sub('[^0-9]', '', value)
    if len(cpf) != 11:
        raise ValidationError('CPF must have 11 digits.', code='invalid')