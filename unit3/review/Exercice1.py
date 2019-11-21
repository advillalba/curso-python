import re

FORMATO_CODIGO = '^(\\d{4})$'
FORMATO_NOMBRE = '^([a-zA-Z0-9]{1,8})$'
FORMATO_PRECIO = '^((?!.*\\.{2,}.*)[0-9\\.?]{8})$'


def is_not_valid_code(cadena: int):
    return not re.match(FORMATO_CODIGO, str(cadena))


def is_not_valid_name(cadena: str):
    return not re.match(FORMATO_NOMBRE, cadena)


def is_not_valid_price(cadena: float):
    return not re.match(FORMATO_PRECIO, str(cadena))


def __split_products__(cadena: str):
    n = 20
    products = [cadena[i:i + n] for i in range(0, len(cadena), n)]
    return products


def __sort_products__(cadena: str) -> str:
    products = __split_products__(cadena)
    products.sort(key=lambda x: x[:4], reverse=False)
    return ''.join(products)


def __retrieve_product__(cadena, codigo: int) -> str:
    _products = __split_products__(cadena)
    _product = None
    i = 0
    while _product is None and i < len(_products):
        if int(_products[i][:4]) == codigo:
            _product = _products[i]
        i += 1

    return _product


def agregar_articulo(cadena: str, tupla) -> str:
    """ Añade un articulo a la cadena y retorna la nueva cadena. """
    if is_not_valid_code(tupla[0]):
        raise Exception('Codigo introducido con formato incorrecto')

    elif is_not_valid_name(tupla[1]):
        raise Exception('El nombre introducido no es valido')

    elif is_not_valid_price(tupla[2]):
        raise Exception('Precio con formato incorrecto')

    if __retrieve_product__(cadena, tupla[0]) is not None:
        raise Exception("El producto ya existe")

    _product = str(tupla[0]) + str(tupla[1]).zfill(8) + str(tupla[2])

    cadena += _product
    cadena = __sort_products__(cadena)
    return cadena



def buscar_articulo(cadena: str, codigo: int) -> str:
    """ Busca un artículo en la cadena y retorna una tupla con sus datos. """
    _product = __retrieve_product__(cadena, codigo)

    if _product is None:
        raise Exception('No se ha encontrado el producto: ', codigo)

    return _product


def eliminar_articulo(cadena: str, codigo: int) -> str:
    """ Elimina un artículo de la cadena y retorna la nueva cadena. """
    _products = __split_products__(cadena)
    _deleted = False
    i = 0

    while not _deleted and i < len(_products):
        if int(_products[i][:4]) == codigo:
            del _products[i]
            _deleted = True
        i += 1

    return ''.join(_products)