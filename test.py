import dill as pickle
from models import Festivo

fichero = open(f"datos/2024-es-gl.dat", 'rb')
datos = pickle.load(fichero)
salida = []
for festivo in datos:
	salida.append(festivo)
for festivo in salida:
	print(festivo.localidad)
