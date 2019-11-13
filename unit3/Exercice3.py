"""
Crear un programa que lea por teclado una cadena y un caracter, y reemplace todos los espacios por el carácter.
Ej.: si se lee "Un archivo de texto" y el caracter "_" debería devolver "Un_archivo_de_texto".
"""


def request_phrase():
    return input('Introduzca una frase: ')


def request_character():
    return input('¿Con que caracter desea reemplazar los espacios? ')


def print_replaced_phrase(_text, _character_for_replace):
    print(_text.replace(' ', _character_for_replace))


text = request_phrase()
character_for_replace = request_character()
print_replaced_phrase(text, character_for_replace)