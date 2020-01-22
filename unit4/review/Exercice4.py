import logging
import random
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')

DISTANCES_A = {'B': 42, 'C': 31, 'D': 130, 'E': 56, 'F': 46, 'G': 12, 'H': 63, 'I': 97, 'J': 45, 'K': 74}
MAX_ITERATION = 900


def new_random_cities() -> list:
    return sorted(random.sample(list(DISTANCES_A), 3))


def get_cities_distance(cities: list) -> int:
    return sum([DISTANCES_A[city] for city in cities])


def closest_distance(cities: list, random_cities: list, iteration: int) -> bool:
    return cities == random_cities or MAX_ITERATION <= iteration


def close_trip(cities: list, iteration: int) -> list:
    logger.info('La iteracion es: %s', iteration)
    random_cities = new_random_cities()
    if closest_distance(cities, random_cities, iteration):
        return cities

    iteration += 1
    cities_distance = get_cities_distance(cities)
    random_cities_distance = get_cities_distance(random_cities)

    if random_cities_distance < cities_distance:
        return close_trip(random_cities, iteration)
    else:
        return close_trip(cities, iteration)


logger.info('La recursion maxima es de: %s', sys.getrecursionlimit())
closer_trip = close_trip(new_random_cities(), 0)
logger.info('El viaje mas corto es: %s', closer_trip)
