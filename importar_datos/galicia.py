import openpyxl
ndalucia.py
from datetime import datetime
ndalucia.py
import dill as pickle
ndalucia.py
import os
ndalucia.py

ndalucia.py
from models.holiday import Festivo
ndalucia.py

ndalucia.py

ndalucia.py
def cargar_datos(fichero_excel, year):
ndalucia.py
	festivos = []
ndalucia.py
	if fichero_excel.name.endswith('.xlsx'):
ndalucia.py
		wb = openpyxl.load_workbook(fichero_excel)
ndalucia.py
		sheet = wb.active
ndalucia.py

ndalucia.py
		##CORRIGE ERRATA
ndalucia.py
		if year == '2024':
ndalucia.py
			sheet["C327"].value = "municipal"
ndalucia.py
			sheet["E327"].value = "Vilalba"
ndalucia.py
		if year == '2025':
ndalucia.py
			sheet["A12"].value = "2025-12-08"
ndalucia.py

ndalucia.py
		for row in sheet.iter_rows(min_row=2, values_only=True):
ndalucia.py
			if isinstance(row[0], str):
ndalucia.py
				fecha = datetime.strptime(row[0], '%Y-%m-%d')
ndalucia.py
			else:
ndalucia.py
				fecha = row[0]
ndalucia.py

ndalucia.py
			init_params = {
ndalucia.py
				'estado': "es",
ndalucia.py
				'fecha': fecha.strftime('%Y-%m-%d'),
ndalucia.py
				'nombre': row[1],
ndalucia.py
				'provincia': None
ndalucia.py
			}
ndalucia.py
			if row[2] == "municipal":
ndalucia.py
				init_params['localidad'] = row[4]
ndalucia.py
				init_params['autonomia'] = 'ga'
ndalucia.py
			elif row[2] == "autonómico":
ndalucia.py
				init_params['autonomia'] = 'ga'
ndalucia.py

ndalucia.py
			festivo = Festivo(**init_params)
ndalucia.py
			festivos.append(festivo)
ndalucia.py
	return festivos
ndalucia.py

ndalucia.py

ndalucia.py
if __name__ == "__main__":
ndalucia.py
	for fichero in os.scandir('fuentes/galicia/'):
ndalucia.py
		in_year = fichero.name.split('.')[0][-4:]
ndalucia.py
		festivos = cargar_datos(fichero, in_year)
ndalucia.py
		with open(f'../datos/{in_year}-es-ga.dat', 'wb') as fichero:
ndalucia.py
			pickle.dump(festivos, fichero)
ndalucia.py
                #retrocompatibilidade con endpoint antigo
ndalucia.py
		with open(f'../datos/{in_year}-es-gl.dat', 'wb') as fichero:
ndalucia.py
			pickle.dump(festivos, fichero)
ndalucia.py
