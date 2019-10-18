import math

"""
Created on 14 oct. 2019

@author: alvaro
"""

x = float(input('El valor de X sera: '))
y = float(input('El valor de Y sera: '))

result = math.pow(x, 3) + (x / (x - y))
print(result)
