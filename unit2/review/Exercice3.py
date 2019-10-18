"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 €
mensuales.
Escribe un programa que pregunte al usuario su edad y sus ingresos mensuales. A continuación debe mostrar por pantalla
 si el usuario tiene que tributar o no.
Aplica los principios de la programación estructurada.
"""

REQUIRED_AGE = 16
REQUIRED_INCOME = 1000  # Euros


def request_user_information():
    return [int(i) for i in input('Introduzca su edad y sus ingresos separados por coma: ').replace(' ', '').split(',')]


def is_tax_applied(user_information):
    if user_information[0] > REQUIRED_AGE and user_information[1] >= 1000:
        print('El usuario debe tributar')
    else:
        print('El usuario debera tributar en ', (REQUIRED_AGE + 1) - user_information[0], ' anio/s')


userInformation = request_user_information()
is_tax_applied(userInformation)
