import logging
from itertools import groupby

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s= %(message)s')


def validate_arguments(countries: dict) -> None:
    if countries is None or len(countries) == 0:
        logger.error('Parametros obligatorios no informados')
        raise Exception('No se han informado parametros')


def sort_by_language(countries) -> [()]:
    """
    Ordena el diccionario introducido usando sus valores
    :param countries: Dicionario a ordenar
    :return: Diccionario ordenado
    """
    return sorted(countries.items(), key=lambda x: x[1])


def emparejar(**kwargs) -> [()]:
    """
    Funcion que recibe un listado de paises con el idioma mas hablado y devuelve un listado de tuplas agrupando los
    paises con el mismo idioma
    :param kwargs: Parametro variable que se utilizara para pasar como argumentos nombres de paises y el idioma mas
    hablado por sus habitantes
    :return: Retorna un listado de tuplas que agrupan los paises con el mismo idioma
    """
    kwargs = sort_by_language(kwargs)
    groups = []
    for language, values in groupby(kwargs, key=lambda x: x[1]):
        values = list(values)
        logger.debug('Idioma %s -> Paises %s', language, values)
        groups.append(tuple([country[0] for country in values]))

    return groups


emparejados = emparejar(España='Español', Francia='Francés', Argentina='Español', Pp='Español', dd='Francés',
                        Italia='Italiano')
logger.info(emparejados)
