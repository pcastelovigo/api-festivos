import re
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
		self.localidad = self.__convert_to_ascii(localidad)

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

	def __convert_to_ascii(self, texto):
		if isinstance(texto, str):
			texto = re.sub(r'\s', '-', texto.strip())
			texto = re.sub(r'\.', '_', texto)
			texto = texto.lower()
			return unidecode(texto)
		return None
