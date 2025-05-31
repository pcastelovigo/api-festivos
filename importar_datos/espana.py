import holidays
import dill as pickle
import os

from models.holiday import Festivo

PAIS = 'ES'
AÑOS = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
OUTPUT_DIR = '../datos'

AUTONOMIAS = [
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

        calendario = holidays.country_holidays(
            PAIS, subdiv=autonomia, years=[año], language="es"
        )

        for fecha, nombre in calendario.items():
            festivo = Festivo(
                fecha=fecha.strftime('%Y-%m-%d'),
                nombre=nombre,
                estado=PAIS.lower(),
                autonomia=autonomia.lower(),
                provincia=None,
                localidad=None
            )
            festivos.append(festivo)

        ruta_salida = os.path.join(OUTPUT_DIR, f'{año}-es-{autonomia.lower()}.dat')
        with open(ruta_salida, 'wb') as f:
            pickle.dump(festivos, f)
