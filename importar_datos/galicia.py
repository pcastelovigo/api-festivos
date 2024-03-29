import openpyxl
from datetime import datetime
import dill as pickle
import re
import os
from unidecode import unidecode


class Festivo:
	"""
	Clase que reune los datos de cada día festivo que esta API es capaz de ofrecer al usuario
	"""

	def __init__(self, fecha, nombre, estado, autonomia=None, provincia=None, localidad=None):
		"""
		Asigna valores iniciales de los atributos
		:param fecha: la fecha
		:param nombre: el nombre oficial del festivo
		:param estado: el codigo ISO de pais
		:param autonomia: el codigo ISO de la autonomia
		:param provincia: el nombre de la provincia
		:param localidad: el nombre de la localidad
		"""
		self.fecha = fecha
		self.nombre = nombre
		self.estado = estado
		self.autonomia = autonomia
		self.provincia = provincia
		self.localidad = localidad

	def json(self):
		"""
		Devuelve los datos del festivo como un diccionario
		:return: el diccionario
		"""
		return {
			'fecha': self.fecha,
			'nombre': self.nombre,
			'estado': self.estado,
			'autonomia': self.autonomia,
			'localidad': self.localidad
		}


def convert_to_ascii(texto):
	texto = re.sub(r'\s', '-', texto)
	texto = re.sub(r'\.', '_', texto)
	texto = texto.lower()
	return unidecode(texto)


def cargar_datos(fichero_excel, year):
	festivos = []
	if fichero.name.endswith('.xlsx'):
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
				init_params['localidad'] = convert_to_ascii(row[4])
				init_params['autonomia'] = 'gl'
			elif row[2] == "autonómico":
				init_params['autonomia'] = 'gl'

			festivo = Festivo(**init_params)
			festivos.append(festivo)
	return festivos


if __name__ == "__main__":
	for fichero in os.scandir('fuentes/galicia/'):
		year = fichero.name.split('.')[0][-4:]
		festivos = cargar_datos(fichero, year)
		with open(f'../datos/{year}-es-gl.dat', 'wb') as fichero:
			pickle.dump(festivos, fichero)
