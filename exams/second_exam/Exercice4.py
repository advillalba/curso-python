import logging
import threading

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')


class Almacen:
    cantidad = 0

    def agregar_productos(self, cantidad):
        with threading.Lock():
            self.cantidad += cantidad

    def retirar_productos(self, cantidad):
        with threading.Lock():
            self.cantidad -= cantidad


almacen = Almacen()

for i in range(0, 10000):
    threading.Thread(target=almacen.agregar_productos, args=(i,), ).start()
    threading.Thread(target=almacen.retirar_productos, args=(i,)).start()

logger.info(almacen.cantidad)
