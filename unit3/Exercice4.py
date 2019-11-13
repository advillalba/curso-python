"""
Crear un programa que lea por teclado una cadena y un caracter, y reemplace todos los dígitos en la cadena por el
carácter. Ej.:si se lee "su clave es: 1540"yel caracter"X"debería devolver "su clave es: XXXX"
"""

import re

def request_phrase():
    return input('Introduzca una frase: ')


def request_character():
    return input('¿Con que caracter desea reemplazar los espacios? ')


def print_replaced_phrase(_text, _character_for_replace):
    print(re.sub('\\d', _character_for_replace, _text))


text = request_phrase()
character_for_replace = request_character()
print_replaced_phrase(text, character_for_replace)
