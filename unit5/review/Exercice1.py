import logging
import re

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')

MAX_REQUEST = 20
YEAR = 'year'
POPULATION = 'population'

FORMAT = {
    'year': '^(\\d+)$',
    'population': '^(\\d+)$'
}
population_years = []
discarted_values = []


def request_population_year_information() -> (int, int):
    information = input('Introduzca el año y la poblacion separados por coma: ')
    information = information.split(',')
    if len(information) != 2:
        logger.error('No se han introducido dos parametros: %s', information)
        raise Exception('Numero de parametros introducidos invalido')

    year = validate_year(information[0])
    population = validate_population(information[1])
    return year, population


def validate_year(year: str) -> int:
    if not re.match(FORMAT['year'], year.strip()):
        logger.error('La fecha introducida tiene un valor incorrecto: %s', year)
        raise Exception('Fecha con formato incorrecto')
    return int(year)


def validate_population(population: str) -> int:
    if not re.match(FORMAT['year'], population.strip()):
        logger.error('La poblacion introducida tiene un valor incorrecto: %s', population)
        raise Exception('poblacion con formato incorrecto')
    return int(population)


def remove_greater_years(population_year: (int, int)) -> list:
    discarted_years = []
    for val in population_years:
        if val[0] > population_year[0]:
            discarted_years.append(population_years.pop())

    return discarted_years


def fill_stacks():
    for n in range(0, MAX_REQUEST):
        population_year = request_population_year_information()
        discarted_years = remove_greater_years(population_year)
        if len(discarted_years) > 0:
            discarted_values.extend(discarted_years)

        population_years.append(population_year)


fill_stacks()
logger.info('Los años y poblaciones añadidos son: %s', population_years)
logger.info('Los años y poblaciones descartados son: %s', discarted_values)
