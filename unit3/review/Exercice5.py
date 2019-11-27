"""
Como comentamos el fichero no tenia el formato correcto en el enunciado, he puesto el siguiente ya que al IBAN le faltaba
un digito:

ingreso;1200.00;12-04-2019T12:07:04
donacion;50.00;11-12-2018T02:03:12
transferencia;ES43204400110030101446897;00.50;07-04-2019T12:07:04

"""
import re
from datetime import datetime

INPUT_FILE = "ingresos.txt"
OUTPUT_FILE = "ingresos_normalizados.txt"
SEPARATOR = ';'
INPUT_DATE_FORMAT = '%d-%m-%YT%H:%M:%S'
ROW_FORMAT = r'^(ingreso|donacion|transferencia);?([A-Z]{2}\d{23,24})?;(\d{2,}\.\d{2,});(\d{2}-\d{2}-\d{4}T\d{2}:\d{2}:\d{2})$'
OPERATION = {
    'ingreso': 'I',
    'donacion': 'D',
    'transferencia': 'T'
}


def _parse_date(date: str) -> str:
    date = datetime.strptime(date, INPUT_DATE_FORMAT)
    return "{:.0f}".format(datetime.timestamp(date))


def _process_file(text: str) -> str:
    rows = text.split('\n')
    formated_rows = []
    for row in rows:
        fields = re.search(ROW_FORMAT, row).groups()
        row = OPERATION[fields[0]] + SEPARATOR + fields[2] + SEPARATOR + _parse_date(fields[3])
        if fields[1]:
            row += SEPARATOR + fields[1]

        formated_rows.append(row)
    return '\n'.join(formated_rows)


# Función que lee todo el contenido de un fichero de texto
# y retorna un string con el contenido
def leer_fichero(ruta_fichero: str):
    with open(ruta_fichero, 'r') as file:
        return file.read()


# Función que escribe un string en un fichero de texto
# sobreescribiendo el fichero
def escribir_fichero(ruta_fichero: str, texto: str):
    with open(ruta_fichero, 'w') as file:
        return file.write(text)


text = leer_fichero(INPUT_FILE)
text = _process_file(text)
escribir_fichero(OUTPUT_FILE, text)
