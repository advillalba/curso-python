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

rain = [12, 34, 10, 23, 25, 27, 12]
SYMBOL = '*'
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def generate_histogram(volumes):
    for i in range(0, 7):
        print(DAYS[i].rjust(9, ' '), ''.rjust(volumes[i], SYMBOL))


generate_histogram(rain)
