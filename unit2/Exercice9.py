"""
Escribe  un  programa  que,mediante  un  bucle,solicite  al  usuario  números enteros,  pero  se  deben  ignorar
 los números negativos.Cuando el usuario escriba un cero debe finalizar el bucle.Después debes mostraral usuario la
 media aritmética de todos los valores positivos.Utiliza instruccionesbreaky continuepara controlar el
 funcionamiento del bucle
"""
import statistics

numbers = []

for i in range(0, 9999999):
    number = int(input('Introduzca un numero: '))
    if number > 0:
        numbers.append(number)
    elif number == 0:
        break
    else:
        continue

print('La media de los numeros introducidos es: ', statistics.mean(numbers))