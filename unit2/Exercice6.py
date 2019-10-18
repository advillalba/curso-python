"""
La siguiente listade números:volumenes =[12, 34, 10, 23, 25, 27, 12]representael volumen de lluvia caídaen cada día de
 la semana. Utiliza un bucle forpara crear un histogramacomoel siguiente:

 Lunes     *************
 Martes    ************************************
 Miercoles ***********
 Jueves    ***********************
 Viernes   *************************
 Sabado    ***************************
 Domingo   ***********
"""


RAIN =[12, 34, 10, 23, 25, 27, 12]
SYMBOL = '*'
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for i in range (0, 6):
    print(DAYS[i].rjust(8, ' '), ''.rjust(RAIN[i], SYMBOL))
