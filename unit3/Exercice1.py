"""
1) Crear un programa que lea por teclado una cadena, y muestre la siguiente información:
    • Imprima los dos primeros caracteres.
    • Imprima los tres últimos caracteres.
    • Imprima dicha cadena cada dos caracteres. Ej.: "recta" debería imprimir "rca"
    • Dicha cadena en sentido inverso. Ej.: "hola mundo" debe imprimir "odnum aloh"
    • Imprima la cadena en un sentido y en sentido inverso. Ej.: "reflejo" imprime "reflejoojelfer".
"""


def request_input():
    return input('Introduzca una palabra: ')


def print_first_characteres(_word: str):
    print('Las primeras dos letras de la palabra son: ', _word[:2])


def is_even(i: int):
    return int('{0:b}'.format(i)[-1:]) == 0


def print_last_characteres(_word: str):
    print('Las ultimas letras de la palabra son: ', _word[-3:])


def print_pair_characteres(_word: str):
    _formatted_word = ''
    _word = list(_word)
    for i in range(0, len(_word)):
        if is_even(i):
            _formatted_word += _word[i]

    print('Las letras pares son: ', _formatted_word)


def revert_word(_word: str):
    print('La palabra del reves es: ', _word[::-1])


def print_word_and_reverted_word(_word: str):
    print('La palabra concatenada es:    ', _word, _word[::-1])


# word = request_input()
word = 'patata'
print_first_characteres(word)
print_last_characteres(word)
print_pair_characteres(word)
revert_word(word)
print_word_and_reverted_word(word)
