"""
Escribe un programa que solicite un texto. A continuación utiliza un bucle para contar el número de vocales que contenga el texto.
"""

VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

text = input('Por favor, introduzca el texto que quiera analizar: ')

countVowels = 0
for vowel in VOWELS:
    countVowels += text.count(vowel)

print('El texto contiene ', countVowels, ' vocales')
