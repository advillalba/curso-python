import logging
import csv
import os

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')

FILE = 'Exercice1Mock.csv'
APPEND = 'a'
WRITE = 'w'


class Product:
    warehouse = None
    name = None
    quantity = None

    def __init__(self, data: [str]) -> None:
        self.warehouse = data[0]
        self.name = data[1]
        self.quantity = data[2]

    def __str__(self) -> str:
        return 'Hay {} del producto {} en el almacén {}'.format(self.quantity, self.name, self.warehouse)


def _init_files_():
    logger.info('Inicializando mocks %s', FILE)
    with open(FILE, 'w') as file:
        file.write('Almacén 1,Caja tornillos,100 unidades\n')
        file.write('Almacén 2,Lubricante,30 litros\n')
        file.write('Almacén 1,Cartón embalaje,5 kilos\n')
        file.write('Almacén 3,Alicates,5 kilos\n')
        file.write('Almacén 3,Caja tornillos,15 kilos\n')


def _search_product(path: str, product_name: str) -> None:
    pass


def _request_product_name():
    return input('\nIntroduzca el nombre del artículo que quiere buscar: ')


def _find_products_(path: str, product_name: str) -> None:
    logger.info('Buscando el producto: %s', product_name)
    products = []

    with open(path, 'r', newline='') as file:
        data = csv.reader(file, delimiter=',')
        for line in data:
            product = Product(line)
            if product_name == product.name:
                products.append(product)
    if len(products) > 0:
        _create_file_products(FILE, products)


def _create_file_products(path: str, products: [Product]) -> None:
    file_name = products[0].name + '.txt'
    absolute_path = os.path.dirname(os.path.abspath(path))
    file_path = os.path.join(absolute_path, file_name)

    file_mode = APPEND if os.path.exists(file_path) else WRITE
    with open(file_path, file_mode) as file:
        writer = csv.writer(file)
        for product in products:
            writer.writerow([product.warehouse, product.name, product.quantity])


_init_files_()
product_name = _request_product_name()
_find_products_(FILE, product_name)
