from fastapi import FastAPI
import dill as pickle

app = FastAPI()

@app.get("/")
async def root():
	return {"estado": "Hola mundo"}

@app.get("/{anho}")
async def read_item(anho):
	return {"estado": 400}

@app.get("/{anho}/{pais}")
async def read_item(anho, pais):
	if pais == "es": region = "gl" # datos por defecto: galicia
	try:
		with open(f"datos/{anho}-{pais}-{region}.dat", 'rb') as fichero:
			datos = pickle.load(fichero)
		salida = []
		for festivo in datos:
			if festivo.localidad is None and festivo.autonomia is None:
				salida.append(festivo)
		return {"estado": 200, "datos": salida }
	except:
		return {"estado": 404}


@app.get("/{anho}/{pais}/{region}")
async def read_item(anho, pais, region):
	try:
		with open(f"datos/{anho}-{pais}-{region}.dat", 'rb') as fichero:
			datos = pickle.load(fichero)
		salida = []
		for festivo in datos:
			if festivo.localidad is None:
				salida.append(festivo)
		return {"estado": 200, "datos": salida }
	except:
		return {"estado": 404}

@app.get("/{anho}/{pais}/{region}/{localidad}")
async def read_item(anho, pais, region, localidad):
	try:
		with open(f"datos/{anho}-{pais}-{region}.dat", 'rb') as fichero:
			datos = pickle.load(fichero)
		salida = []
		f_locales = 0
		for festivo in datos:
			if festivo.localidad is None and (festivo.autonomia == region or festivo.estado == pais):
				salida.append(festivo)
			if festivo.localidad == localidad:
				salida.append(festivo)
				f_locales = f_locales + 1
		if f_locales == 0: return {"estado": 404}
		return {"estado": 200, "datos": salida }
	except:
		return {"estado": 404}
