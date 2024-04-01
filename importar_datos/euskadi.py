import os
import dill as pickle
import openpyxl
from importar_datos.models.holiday import Festivo


def cargar_datos(fichero_excel, year):
	festivos = []
	if fichero_excel.name.endswith('.xlsx'):
		wb = openpyxl.load_workbook(fichero_excel)
		sheet = wb.active

		for row in sheet.iter_rows(min_row=2, values_only=True):
			fecha = row[0]

			init_params = {
				'estado': "es",
				'fecha': fecha.strftime('%Y-%m-%d'),
				'nombre': row[1],

			}
			if not row[5].startswith("Todos"):
				init_params['provincia'] = row[5]
				init_params['autonomia'] = 'pv'

			if row[6]:
				init_params['localidad'] = row[3]

			festivo = Festivo(**init_params)
			festivos.append(festivo)
	return festivos


if __name__ == "__main__":
	for fichero in os.scandir('fuentes/euskadi/'):
		year = fichero.name.split('.')[0][-4:]
		festivos = cargar_datos(fichero, year)
		with open(f'../datos/{year}-es-pv.dat', 'wb') as fichero:
			pickle.dump(festivos, fichero)
