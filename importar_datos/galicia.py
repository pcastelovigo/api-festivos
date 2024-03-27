import openpyxl
from datetime import datetime
import dill as pickle
import re
from unidecode import unidecode

año = 0
festivos = []


class Festivo:
    def __init__(self, fecha, nombre, estado, autonomia, provincia, localidad):
        self.fecha = fecha
        self.nombre = nombre
        self.estado = estado
        self.autonomia = autonomia
        self.provincia = provincia
        self.localidad = localidad

    def json(self):
        return {
            'fecha': self.fecha,
            'nombre': self.nombre,
            'estado': self.estado,
            'autonomia': self.autonomia,
            'localidad': self.localidad
        }


def asciificador(texto):
    texto = re.sub(r'\s', '-', texto)
    texto = re.sub(r'\.', '_', texto)
    texto = texto.lower()
    return unidecode(texto)


def cargar_datos(fichero_excel):
    wb = openpyxl.load_workbook(fichero_excel)
    sheet = wb.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if isinstance(row[0], str):
            fecha = datetime.strptime(row[0], '%Y-%m-%d')
        else:
            fecha = row[0]

        if row[2] == "municipal":
            festivo = Festivo(fecha.strftime('%Y-%m-%d'), row[1], "es", "gl", None, asciificador(row[4]))

        elif row[2] == "autonómico":
            festivo = Festivo(fecha.strftime('%Y-%m-%d'), row[1], "es", "gl", None, None)

        elif row[2] == "estatal":
            festivo = Festivo(fecha.strftime('%Y-%m-%d'), row[1], "es", None, None, None)

        festivos.append(festivo)
    print(fecha.year)
    global año
    año = fecha.year


fichero_excel = "fuentes/calendario_laboral_2024.xlsx"
cargar_datos(fichero_excel)

with open(f'../datos/{año}-es-gl.dat', 'wb') as fichero:
    pickle.dump(festivos, fichero)
