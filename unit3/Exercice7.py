"""
Escribe el código de un módulo "sumador.py". Ese módulo, cuando es ejecutado, debe leer todos los argumentos de la
línea de comando que lo ejecuta, e imprimir la suma de todos aquellos que sean números.
"""

import sys
import re


def find_numbers():
    return [int(arg) if re.match("^(\\d+)$", arg) else 0 for arg in sys.argv]


def print_sum(_numbers: list):
    print(sum(n for n in _numbers))


numbers = find_numbers()
print_sum(numbers)
