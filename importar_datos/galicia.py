import openpyxl
from datetime import datetime
import dill as pickle
import os

from models.holiday import Festivo


def cargar_datos(fichero_excel, year):
	festivos = []
	if fichero_excel.name.endswith('.xlsx'):
		wb = openpyxl.load_workbook(fichero_excel)
		sheet = wb.active

		##CORRIGE ERRATA
		if year == '2024':
			sheet["C327"].value = "municipal"
			sheet["E327"].value = "Vilalba"

		for row in sheet.iter_rows(min_row=2, values_only=True):
			if isinstance(row[0], str):
				fecha = datetime.strptime(row[0], '%Y-%m-%d')
			else:
				fecha = row[0]

			init_params = {
				'estado': "es",
				'fecha': fecha.strftime('%Y-%m-%d'),
				'nombre': row[1],
				'provincia': None
			}
			if row[2] == "municipal":
				init_params['localidad'] = row[4]
				init_params['autonomia'] = 'gl'
			elif row[2] == "autonómico":
				init_params['autonomia'] = 'gl'

			festivo = Festivo(**init_params)
			festivos.append(festivo)
	return festivos


if __name__ == "__main__":
	for fichero in os.scandir('fuentes/galicia/'):
		in_year = fichero.name.split('.')[0][-4:]
		festivos = cargar_datos(fichero, in_year)
		with open(f'../datos/{in_year}-es-gl.dat', 'wb') as fichero:
			pickle.dump(festivos, fichero)
