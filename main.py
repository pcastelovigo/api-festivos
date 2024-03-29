from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import dill as pickle

app = FastAPI()

NATIONAL_DAY, REGION_DAY, LOCAL_DAY = range(3)


@app.get("/version")
async def version() -> dict:
	"""
	Devuelve al usuario el numero de version actual de esta API
	:return: el JSON con el numero de version
	"""
	return {"version": "0.1.0"}


@app.get("/{anho}")
async def read_item(anho):
	raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not supported")


@app.get("/{anho}/{pais}")
@app.get("/{anho}/{pais}/{region}")
@app.get("/{anho}/{pais}/{region}/{localidad}")
async def get_holiday(anho, pais, region=None, localidad=None) -> JSONResponse:
	"""
	Devuelve el objeto JSON con la lista de dias festivos para los parametros entrantes

	:parameter anho: el año como entero (obligado)
	:parameter pais: el codigo ISO de pais (obligado)
	:parameter region: el codigo ISO de comunidad autonoma (opcional), None por defecto
	:parameter localidad: el nombre de localidad (opcional), None por defecto
	:returns la lista de festivos
	"""
	if localidad is not None:
		day_type = LOCAL_DAY
	elif region is not None:
		day_type = REGION_DAY
	else:
		day_type = NATIONAL_DAY
		region = 'gl'
	filename = f"datos/{anho}-{pais}-{region}.dat"
	try:
		result = await build_holidays_list(day_type, filename, localidad)

		f_locales = len([f for f in result if is_only_local(f, localidad)])
		if localidad is not None and f_locales == 0:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Local holidays were not found for city {localidad}")
		return JSONResponse(status_code=status.HTTP_200_OK, content={"datos": result})
	except FileNotFoundError as e:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no data for the requested parameters. File {e.filename} does not exist")


async def build_holidays_list(day_type, filename, localidad):
	"""
	Construye y devuelve la lista de Python conteniendo los festivos:
		NACIONALES
		o
		AUTONOMICOS
		o
		LOCALES
	y coincidiendo con el nombre de la localidad, si no es None

	:param day_type: LOCAL_DAY, REGION_DAY o NATIONAL_DAY
	:param filename: el nombre del fichero del cual se recupera la info
	:param localidad: el nombre de la localidad (opcional), si no es None
	:return: la lista con los festivos como objetos diccionario
	"""
	with open(filename, 'rb') as fichero:
		datos = pickle.load(fichero)
	result = []
	for festivo in datos:
		if day_belongs_to_type(festivo, day_type):
			if festivo.localidad is None or festivo.localidad == localidad:
				result.append(festivo.json())
	return result


def day_belongs_to_type(holiday, dtype):
	"""
	Devuelve si el festivo pertenece al tipo de festivo
	:param holiday: el festivo
	:param dtype: el tipo de festivo (LOCAL, AUTONOMICO o NACIONAL)
	:return: True si el festivo es del tipo, False en otro caso
	"""
	if dtype == LOCAL_DAY:
		return True

	if dtype == REGION_DAY:
		if holiday.localidad is None:
			return True

	if dtype == NATIONAL_DAY:
		if holiday.localidad is None and holiday.autonomia is None:
			return True

	return False


def is_only_local(festivo, localidad):
	"""
	Devuelve si el festivo es de la localidad deseada

	:param festivo: el festivo a inspeccionar
	:param localidad: la localidad deseada
	:return: True si el festivo es de esta localidad, False en otro caso
	"""
	return festivo.get('localidad', None) is not None and festivo['localidad'] == localidad
