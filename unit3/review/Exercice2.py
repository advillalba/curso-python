import re
from datetime import datetime
from time import struct_time

DATE_TIME_FORMAT = '(([012][0-9])|(3[01]))\\-((0[1-9])|(1[012]))\\-(\\d{4})\\s(([01][0-9])|2[0-3])\\:([0-5][0-9])'
PRICE_FORMAT = '((\\d+)(\\.[0-9]{0,2})?)'
DESCRIPTION_FORMAT = '(\\w{1,100})'
ventas_list = []


def __validate__(arg: str, pattern: str) -> bool:
    """ Valida el parametro introducido usando la expresion dada, si no es valido se lanza una excepcion
    :raises Exception:  Parametro con formato incorrecto
    """
    if not re.match(pattern, arg):
        print('Parametro [', arg, '] con formato incorrecto')
        raise Exception('Parametro [', arg, '] con formato incorrecto')
    return arg


def __request_sale__() -> (struct_time, float, str):
    """ Solicita por pantalla un producto """
    date = __validate__(input('Introduzca la fecha con formato dd-mm-yyyy hh:mi: '), DATE_TIME_FORMAT)
    price = __validate__(input('Intoduzca el precio: '), PRICE_FORMAT)
    description = __validate__(input('Introduzca lal descripcion: '), DESCRIPTION_FORMAT)
    return datetime.strptime(date, '%d-%m-%Y %H:%M').timetuple(), float(price), description


def request_sales() -> [(struct_time, float, str)]:
    """ Solicita por pantalla 10 productos """
    sales = []
    for i in range(0, 10):
        sales.append(__request_sale__())

    return sales


def venta_str(venta_tupla: [(struct_time, float, str)]):
    """ Muestra por pantalla los productos introducidos """
    for i in range(0, len(venta_tupla)):
        sale = venta_tupla[i]
        date = struct_time(sale[0])
        date = "{:02d}".format(date.tm_mday) + '-' + "{:02d}".format(date.tm_mon) + '-' + "{:04d}".format(date.tm_year)
        price = sale[1]
        description = sale[2]
        print('Fecha: ', date, '; Precio: ', "{0:.2f}".format(price), '; ', description)


sales = request_sales()
venta_str(sales)
