import logging
import threading

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')


def ejecutar_varias_veces(func_accion, numero_veces=1, argumentos=None):
    if numero_veces > len(argumentos):
        raise Exception('El numero de argumentos no coincide con el numero de iteraciones')
    for i in range(0, numero_veces):
        threading.Thread(target=func_accion, args=(argumentos[i],)).start()


def function(x):
    logger.info('El hilo es %s, tiene el id %s y el argumento es %s ', threading.current_thread().getName(),
                threading.current_thread().ident, x)


ejecutar_varias_veces(function, 3, ['patata', 'pera', 'manzana'])
