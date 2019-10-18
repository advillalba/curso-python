"""
Escribe un programa que solicite al usuario un número mayor que cero. El programa debe garantizar que al final el
usuario introducirá un número válido, para ello volverá a pedirlo hasta que lo que escriba el usuario sea válido.
"""


def ask_number(i=0):
    number = 0
    if i == 0:
        number = int(input('Por favor, introduzca un numero mayor que cero: '))
    else:
        number = int(
            input('Intento numero ' + str(i) + '. El numero introducido es menor que cero, introduzca uno mayor'))

    if number > 0:
        print('Ha terminado el programa')
    else:
        ask_number(i + 1)


ask_number()