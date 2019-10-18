"""
Debe solicitar dos números por pantalla.
Debe calcular la división entre los números.
Si el divisor es cero debe mostrar un mensaje de error, sino debe mostrar el resultado de la división.

Aplica los principios de la programación estructurada.
"""


def request_number(message):
    return int(input(message))


first_number = request_number('Introduzca el primer numero por pantalla: ')
second_number = request_number('Introduzca el segundo numero por pantalla: ')

if second_number == 0:
    print('ERROR: El divisor no puede ser 0')
else:
    print(first_number / second_number)
