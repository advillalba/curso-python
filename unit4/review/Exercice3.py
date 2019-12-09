"""
Debes crear una función llamada valor_medio. Esta función debe recibir como argumentos una lista de números,
y debe retornar el valor mínimo.

Resuelve el algoritmo usando recursividad. Si divides una lista por la mitad, el valor mínimo es el menor de los
valores mínimos de cada sublista.

"""
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')


def valor_medio(*numbers: int) -> int:
    return sorted(numbers)[0]


min = valor_medio(5, 3, 4, 2, 1, 10)
print(mind)
