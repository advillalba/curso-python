"""
Debes crear una función llamada evaluar_vocales. Esta función debe declarar los siguientes parámetros:

• vocales: un parámetro variable que debe permitir pasar un diccionario, cuyas claves sean una vocal y el valor
 asociado sea un número entero (que va a indicar una repetición de la clave).

La función debe solicitar un texto al usuario hasta que simplemente escriba un salto de línea. Cada texto introducido
por el usuario debe ser analizado de forma que hay que informar de si posee tantas vocales como se indica en el
diccionario vocales.
"""
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')


def evaluar_vocales(**vocales):

    text = input('Introduzca un texto: ')
    logger.info('Las vocales son: %s', vowels)
    for vowel, ocurrences in vocales.items():
        if text.count(vowel) != ocurrences:
            logger.error('El texto introducido no contiene %s %s', ocurrences, vowel)
            raise Exception('El texto introducido no contiene', ocurrences, vowel)

    logger.info('El texto es valido')


vowels = {
    'a': 2,
    'i': 3
}
evaluar_vocales(**vowels)
