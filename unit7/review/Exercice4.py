import logging
import os
from enum import Enum

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')

ENCODING = 'UTF-8'
LINE_BREAK = bytes('\n', ENCODING)


class Status(Enum):
    ACTIVE = 'A'
    DELETED = 'D'


def validate_amount(amount):
    if float(amount) > 1000000:
        raise Exception('La cantidad introducida es superior a 1.000.000')


def _decode_bytes_(encoded_record: bytes):
    record = Record
    decoded_data = bytes(encoded_record).decode(ENCODING)
    record.id = int(decoded_data[1:6])
    record.status = Status(decoded_data[0:1])
    record.user_id = decoded_data[6:15]
    record._amount = float(decoded_data[15::])
    return record


class Record:
    _id_ = None
    _status_ = None
    _user_id_ = None
    _amount_ = None

    @property
    def id(self):
        return self._id_

    @id.setter
    def id(self, id: int):
        if len(str(id)) > 5:
            raise Exception('Identificador con formato incorrecto')
        self._id_ = f'{id:05}'

    @property
    def status(self):
        return self._status_

    @status.setter
    def status(self, status):
        if not type(status) is Status:
            raise Exception('El estado introducido no es valido')
        self._status_ = status

    @property
    def user_id(self):
        return self._user_id_

    @user_id.setter
    def user_id(self, user_id: str):
        if (len(user_id)) > 9:
            raise Exception('Usuario con formato incorrecto')

        self._user_id_ = user_id.zfill(9).upper()

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value: float):
        validate_amount(value)
        self._amount = value

    def __init__(self, id: int, user_id: str, amount: float, status: Status = Status.ACTIVE):
        self.id = id
        self.status = status
        self.user_id = user_id
        self._amount = amount

    def __str__(self) -> str:
        return 'Estado: {}, identificador: {}, usuario: {}, cuantia: {}'.format(self.status.name, self.id, self.user_id,
                                                                                self.amount)

    @property
    def byte_representation(self) -> bytes:
        return bytes(self.status.value + str(self.id) + self.user_id + str(self.amount), ENCODING)


class BinaryFileOperation:
    path = None

    def __init__(self, path):
        self.path = path

    def add(self, record: Record):
        logger.info('Se añade el registro: %s', record)
        file_option = 'wb'
        if os.path.exists(self.path):
            file_option = 'ab'

        with open(self.path, file_option) as file:
            file.write(record.byte_representation)
            file.write(LINE_BREAK)

    def remove(self, id) -> Record:
        encoded_id = bytes(id, ENCODING)
        lines = open(self.path, 'rb').readlines()
        with open(self.path, 'wb') as file:
            for line in lines:
                if line[1:6] == encoded_id:
                    line = bytes(Status.DELETED.value, ENCODING) + line[1::]
                    logger.info('Se ha eliminado el registro con identificador %s', id)
                file.write(line)

    def get(self, id: str) -> Record:
        logger.info('Se busca el registro con identificador %s', id)
        encoded_id = bytes(id, ENCODING)
        record = None
        with open(self.path, 'rb') as file:
            line = file.readline()
            while line and record is None:
                if line[1:6] == encoded_id:
                    record = _decode_bytes_(line)
                else:
                    line = file.readline()
        return record

    def update_amount(self, id: str, amount: float):
        validate_amount(amount)
        encoded_id = bytes(id, ENCODING)
        logger.info('Se actualiza el importe  %s del registro con identificador %s', amount, id)
        encoded_amount = bytes(str(amount), ENCODING)
        lines = open(self.path, 'rb').readlines()
        with open(self.path, 'wb') as file:
            for line in lines:
                if line[1:6] == encoded_id:
                    line = line[0:16] + encoded_amount + LINE_BREAK
                    logger.info('Actualizado!')

                file.write(line)

    def list(self, price: float = 0) -> [Record]:
        logger.info('Se buscan los registros con importe superior a %s', price)
        active = bytes(Status.ACTIVE.value, ENCODING)

        result = []
        with open(self.path, 'rb') as file:
            line = file.readline()
            while line:
                if line[0:1] == active and float(bytes(line[16:-1]).decode(ENCODING)) > price:
                    result.append(_decode_bytes_(line))
                line = file.readline()
        return result


if os.path.exists('Exercice4'):
    os.remove('Exercice4')

file = BinaryFileOperation('Exercice4')
file.add(Record(1, 'ñ', 1.0))
file.add(Record(2, 'a', 2.0))
file.add(Record(3, 'b', 4.0))
file.add(Record(4, 'c', 6.0))
file.add(Record(5, 'd', 5.0))
file.add(Record(6, 'e', 2.0))

file.remove('00001')
record = file.get('00003')
logger.info(record)
file.update_amount('00003', 130.1)
logger.info('Se ha encontrado el registro %s', str(file.get('00003')))
records = file.list(0.5)
logger.info('Los registros son: %s', records)
for record in records:
    logger.info(str(record))
