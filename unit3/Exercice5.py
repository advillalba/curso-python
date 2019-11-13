"""
La siguiente lista de números:volumenes = [12, 34, 10, 23, 25,27, 12]representa el volumen de lluvia caída en cada día
de la semana. Utiliza un bucle forpara crear un histograma como el siguiente:
       Lunes                         *************
      Martes  ************************************
   Miercoles                           ***********
      Jueves               ***********************
     Viernes             *************************
      Sabado           ***************************
     Domingo                           ***********

"""

rain = [12, 34, 10, 23, 25, 27, 12]
SYMBOL = '*'
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def generate_histogram(volumes):
    for i in range(0, 7):
        print(f'{DAYS[i]:>10}{"": >{35 - volumes[i]}}{"":{SYMBOL}>{volumes[i]}}')


generate_histogram(rain)
