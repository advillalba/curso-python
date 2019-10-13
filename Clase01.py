import matplotlib.pyplot as plt
import math

'''
Created on 13 oct. 2019

@author: alvaro
'''
first_coordinates = [int(i) for i in
                     input('Por favor, introduzca las primeras coordenadas separando X e Y por una coma: ').split(",")]

second_coordinates = [int(i) for i in
                      input('Por favor, introduzca las segundas coordenadas separando X e Y por una coma: ').split(",")]
plt.scatter(first_coordinates[0], first_coordinates[1])
plt.scatter(second_coordinates[0], second_coordinates[1])
# I get the formula from this website: http://www.matematicatuya.com/GRAFICAecuaciones/S1a.html
distance = str(math.sqrt(((second_coordinates[0] - first_coordinates[0]) ** 2) + (
        (second_coordinates[1] - first_coordinates[1]) ** 2)))
print('La distancia entre los puntos es de: ' + distance)
plt.show()
