import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')


def intercambiar(tupla: (), posicion: int) -> ():
    """
    Retorna una nueva tupla formada por los elementos que van desde posicion hasta el final de tupla,
    seguido de los elementos que hay antes de posicion.
    :param tupla: Tupla inicial que se modificara usando el parametro posicion
    :param posicion: Numero entero usado para modificar la tupla
    :return: Devuelve la tupla inicial reorganizada usando de indice el valor de 'posicion'
    """
    return tupla[posicion:]+tupla[:posicion]


initial_tuple = (1, 2, 3, 4)
logger.info('La tupla inicial es: %s', initial_tuple)

final_tuple = intercambiar(initial_tuple, 2)
logger.info('La nueva tupla es: %s', final_tuple)
