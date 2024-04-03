import os
import dill as pickle
import openpyxl

from models.holiday import Festivo
from workalendar.europe import Asturias


def cargar_datos(fichero_excel, year):
	festivos = set(local_holidays(fichero_excel, year))

	holidays = Asturias(year=year).holidays()
	for day in holidays:
		init_params = {
			'estado': "es",
			'fecha': day[0].strftime('%Y-%m-%d'),
			'nombre': day[1],
			'provincia': 'asturias',
			'autonomia': 'as',
		}
		festivo = Festivo(**init_params)
		festivos.add(festivo)
	return sorted(list(festivos))


def local_holidays(fichero_excel, year):
	festivos_locales = []
	if fichero_excel.name.endswith('.xlsx'):
		wb = openpyxl.load_workbook(fichero_excel)
		sheet = wb.active

		if year == '2024':
			sheet["C142"].value = "2024-02-13"

		for row in sheet.iter_rows(min_row=2, values_only=True):
			if row[0] and row[0].strip().upper() == 'LOCAL':
				fecha = row[2]
				try:
					fecha = fecha.strftime('%Y-%m-%d')
				except AttributeError:
					continue

				init_params = {
					'estado': "es",
					'fecha': fecha,
					'nombre': row[3],
					'provincia': 'asturias',
					'autonomia': 'as',
					'localidad': row[1],
				}
				festivo = Festivo(**init_params)
				festivos_locales.append(festivo)
	return festivos_locales


if __name__ == "__main__":
	for fichero in os.scandir('fuentes/asturias/'):
		in_year = fichero.name.split('.')[0][-4:]
		festivos = cargar_datos(fichero, in_year)
		with open(f'../datos/{in_year}-es-as.dat', 'wb') as fichero:
			pickle.dump(festivos, fichero)
