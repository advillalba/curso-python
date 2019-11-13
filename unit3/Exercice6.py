"""
Solicita un número por pantalla y genera una tabla como la siguiente:
+--------------------+--------------------+--------------------+
|      BASE 10       |       BASE 2       |      BASE 16       |
+--------------------+--------------------+--------------------+
|       1234         |    10011010010     |       4D2          |
+--------------------+--------------------+--------------------+

"""


def request_number():
    return int(input('Introduzca un numero: '))


def print_table(_decimal):
    _binary = f'{_decimal:b}'
    _hex = f'{_decimal:x}'
    _row_size = len(_binary) + 6
    _row_separator = f'{"+":{"-"}<{_row_size}}{"+":{"-"}<{_row_size}}{"+":{"-"}<{_row_size}}+'
    _header = f'|{"BASE 10":^{_row_size-1}}|{"BASE 2":^{_row_size-1}}|{"BASE 64":^{_row_size-1}}|'
    _values = f'|{_decimal:^{_row_size - 1}}|{_binary:^{_row_size - 1}}|{_hex:^{_row_size - 1}}|'

    print(_row_separator)
    print(_header)
    print(_row_separator)
    print(_values)
    print(_row_separator)


number = request_number()
print_table(number)
