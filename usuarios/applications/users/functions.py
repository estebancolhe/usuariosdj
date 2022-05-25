#funciones extra de la aplicacion users

#fucion que genera un codigo alfanumerico de 6 digitos como maximo

import random
import string

def code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))