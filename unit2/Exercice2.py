"""
Escribe un programa que solicite tres números, y a continuación imprime el mayor de ellos.
Usa la estructura if/elif/elsepara resolver este ejercicio.Después sustituye la estructura if/elif/else por una estructura ternaria.
"""


firstNumber = input('Por favor, introduzca el primer numero: ')
secondNumber = input('Por favor, introduzca el segundo numero: ')
thirdNumber = input('Por favor, introduzca el tercer numero: ')


def printGreaterNumber(number):
    print('El numero mas alto es: ', number)


if firstNumber >= secondNumber and firstNumber >= thirdNumber:
    printGreaterNumber(firstNumber)

elif secondNumber >= firstNumber and secondNumber > thirdNumber:
    printGreaterNumber(secondNumber)

else:
    printGreaterNumber(thirdNumber)

firstGreater = firstNumber if firstNumber >= secondNumber else secondNumber
greaterNumber = firstNumber if firstNumber >= thirdNumber else thirdNumber

printGreaterNumber(greaterNumber)