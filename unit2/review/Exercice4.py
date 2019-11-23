"""
Los alumnos de un curso se han dividido en dos grupos, A y B, de acuerdo al sexo y el nombre. El grupo A esta formado
 por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N, y el grupo B por el resto.
Escribe un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
Aplica los principios de la programación estructurada.
"""


def request_user_information():
    return input('Por favor, introduzca su nombre y su sexo separados por coma: ').replace(' ', '').split(',')


def is_first_group(gender, first_name_letter):
    print(gender, first_name_letter)
    return (gender == 'HOMBRE' and first_name_letter > 'N') or (gender == 'MUJER' and first_name_letter < 'M')


def assign_group(user_information):
    first_letter = user_information[0][:1].upper()
    gender = user_information[1].upper()
    if is_first_group(gender, first_letter):
        print('Pertenece al grupo A')
    else:
        print('Pertenece al grupo B')


user_information = request_user_information()
assign_group(user_information)
