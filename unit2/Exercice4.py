"""
Escribe un programa que solicite al usuario que escriba un año. Acontinuación debes decirle si es un año bisiesto o no.
Un año bisiesto es divisible por 4, pero no por 100.
"""

year = int(input('Introduzca el anio: '))

if year % 100 is 0 and year % 4 is 0:
    print('El anio no es bisiesto')
else:
    print('El anio es bisiesto')