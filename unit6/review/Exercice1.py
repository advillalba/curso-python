import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')


class Luminaria:
    intensidad = None
    color = None

    def __init__(self, intensidad: int = 0, color: str = 'blanco'):
        self.intensidad = intensidad
        self.color = color

    def estaApagada(self) -> bool:
        return self.intensidad == 0


class Bombilla:
    marca = None
    luminaria = None

    def __init__(self, marca: str, luminaria: Luminaria = Luminaria()):
        self.marca = marca
        self.luminaria = luminaria


bombilla1 = Bombilla('Thompson', Luminaria(15, 'verde'))
bombilla2 = Bombilla('Phillips')
logger.info('La bombilla1 es de %s tiene un color %s y esta %s', bombilla1.marca, bombilla1.luminaria.color,
            'apagada' if bombilla1.luminaria.estaApagada() else 'encendida')
logger.info('La bombilla2 es de %s tiene un color %s y esta %s', bombilla2.marca, bombilla2.luminaria.color,
            'apagada' if bombilla2.luminaria.estaApagada() else 'encendida')
