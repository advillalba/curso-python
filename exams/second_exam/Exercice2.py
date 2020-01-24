import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')
ENCODING = 'UTF-8'
SEPARATOR = '|'
FILE_NAME = 'Exercice2FileExample.txt'


class Automovil:
    trademark = None
    _power_ = None
    _seats_ = None

    @property
    def power(self) -> int:
        return self._power_

    @power.setter
    def power(self, value):
        if type(value) is not int:
            value = int(value)
        self._power_ = value

    @property
    def seats(self) -> int:
        return self._seats_

    @seats.setter
    def seats(self, value: int):
        if type(value) is not int:
            value = int(value)

        if value < 1:
            raise Exception('El automovil debe tener al menos un asiento')
        self._seats_ = value

    def __init__(self):
        self.seats = 1

    def serializa(self, ruta_fichero: str):
        if self.trademark is None or self.power is None:
            raise Exception('Los atributos del objeto automovil no estan correctamente informados')
        with open(ruta_fichero, 'wb') as file:
            file.write(bytes(self.trademark + SEPARATOR + str(self.power) + SEPARATOR + str(self.seats), ENCODING))

    def deserializa(self, ruta_fichero: str):
        with open(ruta_fichero, 'rb') as file:
            line = file.readline()
            decoded_line = bytes(line).decode(ENCODING).split(SEPARATOR)
            self.trademark, self.power, self.seats = decoded_line

    def __str__(self) -> str:
        return 'El coche de {} tiene {} CV de potencia y {} asientos'.format(self.trademark, self.power, self.seats)


automovil = Automovil()
automovil.power = 120
automovil.trademark = 'Audi'
automovil.seats = 3
logger.info('Automovil: %s', automovil)
automovil.serializa(FILE_NAME)
automovil_2 = Automovil()
automovil_2.deserializa(FILE_NAME)
logger.info('Automovil 2: %s', automovil_2)
