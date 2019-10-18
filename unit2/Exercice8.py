"""
Escriba  un  programa  que  solicite  al  usuario  que  escriba  un  número  binariode  8  bitsen  forma  de  cadena;
por ejemplo:00101000. Acontinuación muéstrale el número entero (en base 10)correspondiente.
"""

binaryNumber = input('Escriba un numero en binary con un maximo de 8 posiciones: ')


def throwError(number):
    print('El numero ', number, ' tiene mas de 8 posiciones')


if len(binaryNumber) > 8:
    throwError(binaryNumber)
else:
    print('El numero decimal es: ', int(binaryNumber, 2))
