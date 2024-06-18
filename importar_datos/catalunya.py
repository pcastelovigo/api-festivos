import csv
import os
import datetime as dt

import dill as pickle
from models.holiday import Festivo
from workalendar.europe import Catalonia


def cargar_datos(fichero, year):
    festivos = set(local_holidays(fichero, year))

    holidays = Catalonia(year=year).holidays()
    for day in holidays:
        init_params = {
            'estado': "es",
            'fecha': day[0].strftime('%Y-%m-%d'),
            'nombre': day[1],
            'autonomia': 'ct',
        }
        festivo = Festivo(**init_params)
        festivos.add(festivo)
    return sorted(list(festivos))


def local_holidays(fichero, year):
    festivos_locales = []
    if fichero.name.endswith('.csv'):
        with open(fichero, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Any calendari'] == year and row['Festiu'].strip() == 'Festa local':

                    date_as_datetime = dt.datetime.strptime(row['Data'], '%d/%m/%Y')
                    init_params = {
                        'estado': "es",
                        'fecha': date_as_datetime.strftime('%Y-%m-%d'),
                        'autonomia': 'ct',
                        'nombre': '',
                        'localidad': row['Ajuntament o nucli municipal '],
                    }
                    festivo = Festivo(**init_params)
                    festivos_locales.append(festivo)
    return festivos_locales


if __name__ == "__main__":
    for fichero in os.scandir('fuentes/catalunya/'):
        in_year = fichero.name.split('.')[0][-4:]
        festivos = cargar_datos(fichero, in_year)
        with open(f'../datos/{in_year}-es-ct.dat', 'wb') as fichero:
            pickle.dump(festivos, fichero)
