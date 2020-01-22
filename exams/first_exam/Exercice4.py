import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')


def _lower_values(numeros: [int], searched_value: int) -> []:
    return [numero for numero in numeros if numero > searched_value]


def get_sorted_list(numeros: [int]) -> [(int, float)]:
    logger.info("1) Obten una lista ordenada de tuplas. Cada tupla debe contener un numero de la lista y su mitad.")
    result = sorted([(numero, float(numero / 2)) for numero in numeros], key=lambda pair: pair[0])
    logger.info('Resultado: %s', result)
    return result


def get_dictionary(numeros: [int]) -> {}:
    logger.info("2) Obten un diccionario, donde cada clave sera un numero de la lista, y el valor asociado a cada "
                "clave sera una lista con aquellos numeros que sean menores que la clave.")
    output = {}
    for numero in numeros:
        output[numero] = _lower_values(numeros, numero)

    logger.info('Resultado: %s', output)
    return output


def get_tuple_greater_numbers(numeros: [int]) -> ():
    logger.info("3) Obten una tupla con aquellos numeros que sean mayores que el numero que esta antes que el en la "
                "lista. En este caso concreto debe obtenerse (329, 68)")
    result = []
    for i in range(1, len(numeros)):
        if numeros[i] > numeros[i - 1]:
            result.append(numeros[i])

    logger.info('Resultado: %s', result)
    return result


numeros = [124, 329, 24, 68, 45]
get_sorted_list(numeros)
get_dictionary(numeros)
get_tuple_greater_numbers(numeros)
