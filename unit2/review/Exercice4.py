"""
Los alumnos de un curso se han dividido en dos grupos, A y B, de acuerdo al sexo y el nombre. El grupo A esta formado
 por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N, y el grupo B por el resto.
Escribe un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
Aplica los principios de la programación estructurada.
"""

FEMALE_NAME_GROUP_A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
MALE_NAME_GROUP_A = ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def request_user_information():
    return input('Por favor, introduzca su nombre y su sexo separados por coma: ').replace(' ', '').split(',')


def assign_group(user_information):
    first_letter = user_information[0][:1].upper()
    print(first_letter)
    print(user_information[1].upper())
    if user_information[1].upper() == 'HOMBRE' and first_letter in MALE_NAME_GROUP_A or \
            (user_information[1].upper() == 'MUJER' and first_letter in FEMALE_NAME_GROUP_A):
        print('Pertenece al grupo A')
    else:
        print('Pertenece al grupo B')


user_information = request_user_information()
assign_group(user_information)
