"""
Solicita que el usuario escriba una palabra. Acontinuación debes decirle si es un palíndromos;es decir,unapalabraque
stienen el mismo aspecto escritaal revés. Por ejemplo,la palabra "radar"es un palíndromo.
"""

word = input('Escriba el posible palindromo: ')


def invert_word(word_to_invert):
    splited_word = list(word_to_invert)
    inverted_word = ''
    for i in range(len(splited_word) - 1, -1, -1):
        inverted_word += splited_word[i]
    print('La palabra invertida es ', inverted_word)
    return inverted_word


if invert_word(word) == word:
    print('¡Es un palindromo!')
else:
    print('No es un palindromo')
