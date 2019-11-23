import re
import calendar

MONTH_FORMAT = '^((0[0-9])|(1[012]))$'
YEAR_FORMAT = '^(\\d{4})$'


def __validate__(arg: str, pattern: str):
    """ Valida el parametro introducido usando la expresion dada, si no es valido se lanza una excepcion
       :raises Exception:  Parametro con formato incorrecto
       """
    if not re.match(pattern, arg):
        print('Parametro [', arg, '] con formato incorrecto')
        raise Exception('Parametro [', arg, '] con formato incorrecto')
    return arg


def request_date() -> (int, int):
    """ Solicita por pantalla un mes y un año"""
    month = __validate__(input('Introduzca el mes: '), MONTH_FORMAT)
    year = __validate__(input('Introduzca el año: '), YEAR_FORMAT)
    return int(year), int(month)


def print_sundays(year: int, month: int):
    """ Imprime por pantalla los días que caen en domingo del mes y año dados"""
    month_calendar = calendar.Calendar(calendar.MONDAY).monthdayscalendar(year, month)
    sundays = []
    for week in month_calendar:
        if week[6] != 0:
            sundays.append('{:02d}'.format(week[6]))

    print('Los dias que son domingo son:', ', '.join(sundays))


year, month = request_date()
print_sundays(year, month)
