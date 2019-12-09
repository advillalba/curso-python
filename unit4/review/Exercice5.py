import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')


def acumular(valor_inicial, list_valores, func_acumulador, list_parcial, func_parcial, func_finalizador):
    ac = valor_inicial
    for v in list_valores:
        func_parcial(v, list_parcial)
        ac = func_acumulador(ac, v)
    return func_finalizador(ac, list_parcial)


valores = [1, 4, 5, 10, 2, 6, 7, 8, 9, 3, 11, 12]
mean_value = acumular(0, valores, lambda x, y: (x + y) / 2, [], lambda x, y: (x + y) / 2, )
