import re

FULL_NAME_FORMAT = '^([a-zA-Z]+)\\s([a-zA-Z]+)\\s?([a-zA-Z]+)?\\s?([a-zA-Z]+)?$'


def __validate__(arg: str, pattern: str) -> str:
    """ Valida el parametro introducido usando la expresion dada, si no es valido se lanza una excepcion
       :raises Exception:  Parametro con formato incorrecto
       """
    if not re.match(pattern, arg):
        print('Parametro [', arg, '] con formato incorrecto')
        raise Exception('Parametro [', arg, '] con formato incorrecto')
    return arg


def request_full_name() -> str:
    """ Solicita por pantalla el nombre completo """
    full_name = __validate__(input('Introduzca su nombre completo: '), FULL_NAME_FORMAT)
    return full_name


def split_full_name(full_name: str):
    """ Divide en nombre y apellidos el nombre completo introducido """
    elements = re.search(FULL_NAME_FORMAT, full_name)
    if elements.group(4) is not None:
        print('El nombre es:', elements.group(1), elements.group(2), 'y los apellidos son:', elements.group(3),
              elements.group(4))

    elif elements.group(3) is not None:
        print('El nombre es:', elements.group(1), 'y los apellidos son:', elements.group(2), elements.group(3))

    else:
        print('El nombre es:', elements.group(1), 'y el apellido es:', elements.group(2))


full_name = request_full_name()
split_full_name(full_name)
