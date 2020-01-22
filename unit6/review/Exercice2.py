import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')


class Carta(object):
    _card_values_ = {
        'As': 11,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        'sota': 10,
        'caballo': 10,
        'rey': 10
    }

    palo = None
    figura = None
    puntuacion = None

    _palos_ = ['copas', 'espadas', 'bastos', 'oros']

    def _get_punctuation_(self):
        return self._card_values_[self.figura]

    def __init__(self, palo: str, figura: str):
        if palo not in self._palos_:
            raise Exception('El tipo de palo no es valido')
        if figura not in self._card_values_:
            raise Exception('El tipo de figura introducido no es valido')

        self.palo = palo
        self.figura = figura

    def __getattribute__(self, item):
        if item == 'puntuacion':
            return self._get_punctuation_()
        else:
            return object.__getattribute__(self, item)

    def str_display(self) -> str:
        return str(self.figura) + ' de ' + self.palo + ' vale ' + str(self.puntuacion) + ' puntos'


carta = Carta('oros', 2)
carta.figura = 3
logger.info(carta.str_display())
