from random import randint
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')

productoslist = [("Producto{}".format(randint(1, 1000)), i * randint(1, 1000)) for i in range(1, 100)]

logger.info(productoslist)


def sort_tuples_by_price(products: list) -> list:
    logger.info('Consulta 1')
    return sorted(products, key=lambda product: product[1], reverse=False)


def get_non_duplicated_sorted_prices(products: list) -> set:
    logger.info('Consulta 2')
    return set([product[1] for product in products])


def get_product_names(products: list) -> str:
    logger.info('Consulta 3')
    return ', '.join([product[0] for product in products])


def get_product_names_with_odd_price(products: list) -> list:
    logger.info('Consulta 4')
    return [product[0] for product in products if product[1] % 1 == 0]


def get_most_expensive_product(products: list) -> ():
    logger.info('Consulta 5')
    return sorted(products, key=lambda product: product[1], reverse=True)[0]


def are_all_prices_greater_500(products: list) -> bool:
    logger.info('Consulta 6')
    cheap_product = next(filter(lambda product: product[1] < 500, products))
    logger.info('El producto %s cuesta %s', cheap_product[0], str(cheap_product[1]))
    return cheap_product is None


def are_any_product_lower_than_500(products: list) -> bool:
    logger.info('Consulta 6')
    cheap_product = next(filter(lambda product: product[1] < 500, products))
    logger.info('El producto %s cuesta %s', cheap_product[0], str(cheap_product[1]))
    return cheap_product is not None


def get_mean_price(products: list) -> float:
    logger.info('Consulta 8')
    return sum(product[1] for product in products) / len(products)


logger.info(sort_tuples_by_price(productoslist))
logger.info(get_non_duplicated_sorted_prices(productoslist))
logger.info(get_non_duplicated_sorted_prices(productoslist))
logger.info(get_product_names(productoslist))
logger.info(get_product_names_with_odd_price(productoslist))
logger.info(get_most_expensive_product(productoslist))
logger.info(str(are_all_prices_greater_500(productoslist)))
logger.info(str(are_any_product_lower_than_500(productoslist)))
logger.info("{0:.2f}".format(get_mean_price(productoslist)))
