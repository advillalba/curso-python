"""
Escribe un programa que haga lo siguiente:

    Solicita por pantalla el anio en curso.
    Solicita el nombre y anio de nacimiento de tres personas.
    Imprime por pantalla el nombre y edad actual de cada persona.

Aplica los principios de la programación estructurada.
"""


def request_course_year():
    return int(input('Por favor, introduza el anio en curso: '))


def request_person_information():
    name = input('Introduzca su nombre: ')
    birthday = input('Introduzca su anio de nacimiento con formato YYYY-MM-DD: ')
    return name, birthday


def print_person_information(year, person_information):
    print('La persona se llama: ', person_information[0])
    print('Tiene', year - int(person_information[1][:4]))


current_year = request_course_year()
first_person = request_person_information()
second_person = request_person_information()
third_person = request_person_information()

print_person_information(current_year, first_person)
print_person_information(current_year, second_person)
print_person_information(current_year, third_person)
