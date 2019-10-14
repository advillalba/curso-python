import matplotlib.pyplot as plt
import math

"""
Created on 13 oct. 2019

@author: alvaro
"""
FIRST_REQUEST = 'Por favor, introduzca las primeras coordenadas separando X e Y por una coma: '
SECOND_REQUEST = 'Por favor, introduzca las segundas coordenadas separando X e Y por una coma: '


# Formula: http://www.matematicatuya.com/GRAFICAecuaciones/S1a.html
def calculate_distance(point_a, point_b):
    x = point_b[0] - point_a[0]
    y = point_b[1] - point_a[1]
    distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    return distance


pointA = [float(i) for i in input(FIRST_REQUEST).split(",")]
pointB = [float(i) for i in input(SECOND_REQUEST).split(",")]

plt.scatter(pointA[0], pointA[1])
plt.scatter(pointB[0], pointB[1])

print('La distancia entre los puntos es de: ' + str(calculate_distance(pointA, pointB)))
plt.show()
