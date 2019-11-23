"""
Created on 14 oct. 2019

@author: alvaro
"""
IVA = 0.21
productName = input('¿Cual es el nombre del producto? ')
productPrice = float(input('¿Que precio tiene? '))

print('El producto ' + productName + ' tiene un coste total de: ' + str(productPrice + (productPrice * IVA)))
