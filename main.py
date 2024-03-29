from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import dill as pickle

app = FastAPI()

NATIONAL_DAY, REGION_DAY, LOCAL_DAY = range(3)


@app.get("/version")
async def version():
	return {"version": "0.1.0"}


@app.get("/{anho}")
async def read_item(anho):
	return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"reason": "Not supported"})


@app.get("/{anho}/{pais}")
@app.get("/{anho}/{pais}/{region}")
@app.get("/{anho}/{pais}/{region}/{localidad}")
async def get_holiday(anho, pais=None,region=None,localidad=None):
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

		f_locales = len([f for f in result if is_only_local(f, localidad)] )
		if localidad is not None and f_locales == 0:
			return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"reason": f"Local holidays were not found for city {localidad}"})
		return JSONResponse(status_code=status.HTTP_200_OK, content={"datos": result})
	except FileNotFoundError as e:
		return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"reason": f"There is no data for the requested parameters. File {e.filename} does not exist"})


async def build_holidays_list(day_type, filename, localidad):
	with open(filename, 'rb') as fichero:
		datos = pickle.load(fichero)
	result = []
	for festivo in datos:
		if get_day_by_type(festivo, day_type):
			if festivo.localidad is None or festivo.localidad == localidad:
				result.append(festivo.json())
	return result


def get_day_by_type(holiday, dtype):
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
	return festivo.get('localidad', None) is not None and festivo['localidad'] == localidad
