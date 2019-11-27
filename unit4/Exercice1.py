"""
1) Debes crear una función llamada calcular_perimetro. Esta función recibirá como argumento una secuencia de
pares de coordenadas (como tuplas con el valor en las coordenadas X e Y), donde cada par determina un vértice
de una figura geométrica. Utiliza parámetros variables en vez de parámetros fijos.
La función debe retornar el perímetro de la figura geométrica. La distancia entre dos puntos (x1, y1) y (x2, y2) se
calcula con la fórmula:
"""
import math


def calcular_perimetro(*coords: (int, int)):
    if len(coords) < 2:
        raise Exception('Numero de parametros invalidos')

    def calc_distancia(x1: float, y1: float, x2: float, y2: float):
        return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

    result = 0
    for i in range(0, len(coords) - 1):
        x1 = float(coords[i][0])
        y1 = float(coords[i][1])
        x2 = float(coords[i + 1][0])
        y2 = float(coords[i + 1][1])
        result += calc_distancia(x1, y1, x2, y2)
    return result


perimetro = calcular_perimetro((1, 2), (3, 4), (5, 6))
print('El perimetro es:', str(perimetro))
