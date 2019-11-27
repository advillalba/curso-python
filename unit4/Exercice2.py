"""
2) Crea dos funciones:
def solicitar_palabras( n ):
Debe solicitar por pantalla n palabras y retornar una tupla con todas las palabras válidas.
Si el usuario no escribe una palabra (porque contiene espacios en blanco o signos de puntuación)
no se tendrá en cuenta en el conteo.

def palabras_mas_cortas( n, *palabras ):

Recibe como argumentos un número n y una secuencia de palabras. Debe retornar una lista con las n palabras más cortas.

Completa las instrucciones de estas dos funciones y después ejecútalas una a continuación de la otra. Los
argumentos de la función palabras_mas_cortas serán: la mitad del valor pasado en solicitar_palabras y la tupla
devuelta por esta función.
"""
import re


def solicitar_palabras(*n: str) -> [str]:
    print(' '.join(n[0]))
    words = re.findall('([a-zA-Z]+)', ' '.join(n[0]))

    return words


def palabras_mas_cortas(n: int, *palabras: str):
    words = solicitar_palabras(palabras)
    words.sort(key=lambda x: len(x), reverse=False)

    return words[:n]


palabras = palabras_mas_cortas(3, 'pepe', 'a', 'dos', 'casa', 'ameli', 'a', 'de')
print(palabras)
