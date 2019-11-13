"""
Solicita por pantalla la fecha de nacimiento de una persona con el formato “día-mes-año”. Después muestra al usuario
 qué edad tiene en años y días, y en qué día de la semana (entre lunes y domingo) y en qué mes(entre enero y diciembre)
 nació.
"""
from datetime import datetime
import locale
import re

locale.setlocale(locale.LC_ALL, "")


def is_not_valid_date(_date: str):
    return not re.match(r'^\d{2}-\d{2}-\d{4}$', _date)


def request_date():
    #     _date = input('Introduzca la fecha de nacimiento en formato DD-MM-YYYY: ')
    _date = '21-05-1994'
    if is_not_valid_date(_date):
        raise Exception('Formato de fecha no valido')

    return datetime.strptime(_date, '%d-%m-%Y')


def print_age(_birthday: datetime):
    today = datetime.now()
    age = today - _birthday
    print('Tu edad en dias es:', age.days)
    print('Tu edad en años es:', int(age.days / 365))


def print_birthday(_birthday: datetime):
    print('Naciste un', _birthday.strftime('%A'), 'en', _birthday.strftime('%B'))


birthday = request_date()
print_age(birthday)
print_birthday(birthday)
