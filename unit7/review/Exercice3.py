import logging
import re

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')
pattern = "[\\s,\\.:]+([a-zA-Z0-9\\,\\s]+)\\."
name_pattern = "NOMBRE" + pattern
address_pattern = "DIRECCION" + pattern
phone_pattern = "TELEFONO" + pattern
seniority_pattern = "ANTIGUEDAD" + pattern


class Person:
    name = None
    address = None
    phone = None
    seniority = None

    def __init__(self, name, address, phone, seniority):
        self.name = name
        self.address = address
        self.phone = phone
        self.seniority = int(seniority)

    def __str__(self):
        return 'Nombre: {}, Direccion: {}, Telefono: {}, Antigüedad: {}'.format(self.name, self.address, self.phone,
                                                                                self.seniority)


def _file_read(ruta: str) -> [Person]:
    persons = []
    with open(ruta, 'r') as file:
        for line in file:
            name = re.findall(name_pattern, line)[0]
            address = re.findall(address_pattern, line)[0]
            phone = re.findall(phone_pattern, line)[0]
            seniority = re.findall(seniority_pattern, line)[0]

            person = Person(name, address, phone, seniority)
            persons.append(person)

    return persons


def _init_file_():
    with open('Exercice3FileExample.txt', 'w') as file:
        file.write('NOMBRE, pepe. DIRECCION. Alcala 20. TELEFONO: 123456789. ANTIGUEDAD: 33.\n')
        file.write('NOMBRE, juan. TELEFONO: 123456729. ANTIGUEDAD: 40. DIRECCION. Alcala 21.\n')
        file.write('ANTIGUEDAD: 41.NOMBRE, carlos. DIRECCION. Alcala 22. TELEFONO: 123456749.\n')
        file.write('DIRECCION. Alcala 23. TELEFONO: 123456779. ANTIGUEDAD: 42. NOMBRE, alberto.\n')


def seleccionarNombres(ruta_fichero: str) -> [str]:
    return [person.name for person in _file_read(ruta_fichero)]


def seleccionarPorAntiguedad(ruta_fichero: str, antiguedad: int):
    return [[person.name, person.phone] for person in _file_read(ruta_fichero) if person.seniority > antiguedad]


def maximaAntiguedad(ruta_fichero: str) -> int:
    return sorted([person.seniority for person in _file_read(ruta_fichero)], reverse=True)[0]


file_path = 'Exercice3FileExample.txt'
_init_file_()
names = seleccionarNombres(file_path)
logger.info('Los nombres son %s', names)

seniors = seleccionarPorAntiguedad(file_path, 40)
logger.info('Los mas antiguos de 40 años son: %s', seniors)

oldest = maximaAntiguedad(file_path)
logger.info('La mayor antigüedad es de: %s', oldest)
