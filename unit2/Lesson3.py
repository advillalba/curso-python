"""
Un club quiere un programa para registrar socios. Entonces solicita los datos personales:
 + Nombre
 + Direccion
 + Telefono
 + Edad

La cuota mensual es de 100 euros, pero si el socio tiene mas de 60 anios se aplica un descuento
del 10%.

El programa debe solicitar los datos, calcular la cuota mensual y la imprimira por pantalla.

    1. Definir las estructuras de datos globales, y declarar las variables. Los datos
       literales se asignan a variables globales.
"""

# Datos literales
FEE = 100  # Euros
AGE_FOR_DISCOUNT = 60
DISCOUNT = 0.1

# Datos globales
person_information = None
age = int(input('¿Cuantos años tiene? '))


# Algoritmo

# person_information <- Solicitar datos personales

# age <- solicitar edad

# cuota <- Calcular la cuota <- edad
# imprimir_cuota <- cuota

def request_person_information():
    name = input('Por favor, introduzca su nombre: ')
    direction = input('¿Cual es su direccion? ')
    mobile = input('Introduzca su numero de telefono: ')
    return name, direction, mobile


def request_age():
    return int(input('¿Cuantos años tiene? '))


def calculate_fee(age):
    monthly_fee = FEE
    if age > 60:
        monthly_fee = FEE * (1 - DISCOUNT)
    return monthly_fee


def print_fee(fee):
    print(fee)


person_information = request_person_information()
age = request_age()
fee = calculate_fee(age)
print_fee(fee)
