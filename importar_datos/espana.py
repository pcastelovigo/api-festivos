import holidays
import dill as pickle
import os

from models.holiday import Festivo

PAIS = 'ES'
AÑOS = range(2020, 2051)
OUTPUT_DIR = '../datos'

AUTONOMIAS = [
    'GA',  # Galicia
    'AN',  # Andalucía
    'AR',  # Aragón
    'AS',  # Asturias
    'CB',  # Cantabria
    'CE',  # Ceuta
    'CL',  # Castilla y León
    'CM',  # Castilla-La Mancha
    'CN',  # Canarias
    'CT',  # Cataluña
    'EX',  # Extremadura
    'IB',  # Islas Baleares
    'MC',  # Murcia
    'MD',  # Madrid
    'ML',  # Melilla
    'NC',  # Navarra
    'PV',  # País Vasco
    'RI',  # La Rioja
    'VC',  # Comunidad Valenciana
]

os.makedirs(OUTPUT_DIR, exist_ok=True)

for autonomia in AUTONOMIAS:
    for año in AÑOS:
        festivos = []

        festivos_nacionales = holidays.country_holidays(PAIS, years=[año], language="es")

        calendario = holidays.country_holidays(
            PAIS, subdiv=autonomia, years=[año], language="es"
        )

        for fecha, nombre in calendario.items():
            if fecha in festivos_nacionales:
                autonomia_final = None
            else:
                autonomia_final = autonomia.lower()

            festivo = Festivo(
                fecha=fecha.strftime('%Y-%m-%d'),
                nombre=nombre,
                estado=PAIS.lower(),
                autonomia=autonomia_final,
                provincia=None,
                localidad=None
            )
            festivos.append(festivo)
        ruta_salida = os.path.join(OUTPUT_DIR, f'{año}-es-{autonomia.lower()}.dat')
        with open(ruta_salida, 'wb') as f:
            pickle.dump(festivos, f)
