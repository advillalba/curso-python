"""
Debes solicitar por pantalla la información de una vivienda. Esta información debe escribirse en una única línea con el
siguiente formato: <código de la vivienda>;<dirección de la vivienda>;<precio>
El código de la vivienda tendrá siempre 5 caracteres, y el precio será un número entero que ocupará siempre
8 caracteres.  La  dirección  tendrá  una  longitud  variable.  Por  ejemplo,  una  información  válida  será:
"23231;Calle Estrada, sección 7, parcela B;00345000"
Una  vez  solicitada  la  línea  de  información  utiliza  la  técnica  de  recortes  con  strings  para  separar
cada  dato  e imprimirlo por pantalla.
"""
import re

HOUSE_INFORMATION_PATTERN = "([0-9]{5});([a-zA-Z0-9\\,\\.\\sáéíóú]+);([0-9]{8})"


def valid_house_information(_house_information):
    return re.match(HOUSE_INFORMATION_PATTERN, _house_information) is not None


def request_house_information():
    _house_information = input('Introduzca la informacion de la vivienda: ')
    if not valid_house_information(_house_information):
        raise Exception('La informacion introducida tiene un formato incorrecto')

    return _house_information


def print_house_information(_house_information: str):
    _first_splitter = _house_information.index(';')
    _second_splitter = house_information.index(';',_first_splitter+1)
    print('El codigo de la vivienda es: ', _house_information[0:_first_splitter])
    print('La direccion es: ', _house_information[_first_splitter+1:_second_splitter])
    print('El precio: ', house_information[_second_splitter+1:])
    pass


house_information = request_house_information()
print_house_information(house_information)
