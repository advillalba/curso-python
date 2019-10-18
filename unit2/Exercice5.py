"""
Escriba un programa que solicite al usuario su nombre. Acontinuación debes imprimirlo en una líneaque ocupe 60
caracteres de forma que quede alineado a la derechay por la derecha se rellene con puntos.
"""

LINE_LENGTH = 60
SYMBOL = '.'

name = input('Introduzca su nombre: ')

print(name.rjust(LINE_LENGTH, SYMBOL))
