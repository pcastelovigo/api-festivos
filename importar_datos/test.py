import openpyxl
from datetime import datetime
import dill as pickle
import os
from unidecode import unidecode
import re

from models.holiday import Festivo

def __convert_to_ascii(texto):
	if isinstance(texto, str):
		texto = re.sub(r'\s', '-', texto.strip())
		texto = re.sub(r'\.', '_', texto)
		texto = texto.lower()
		return unidecode(texto)
	return None


def cargar_datos(fichero_excel, year):
	festivos = []
	wb = openpyxl.load_workbook(fichero_excel)
	sheet = wb.active

	##CORRIGE ERRATA
	if year == '2024':
		sheet["C327"].value = "municipal"
		sheet["E327"].value = "Vilalba"
	if year == '2025':
		sheet["A12"].value = "2025-12-08"

	lista = []
	for row in sheet.iter_rows(min_row=2, values_only=True):
		if row[2] == "municipal":
			nombre_ascii = __convert_to_ascii(row[4])
			if nombre_ascii not in lista:
				print("('" + nombre_ascii + "', '" + row[4] + "'),")
				lista.append(nombre_ascii)




cargar_datos('fuentes/galicia/2025.xlsx', 2025)

