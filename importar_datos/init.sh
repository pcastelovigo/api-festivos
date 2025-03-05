#!/bin/bash
cd "$(dirname "$0")"

# Descarga de CCAAs
curl -k --create-dirs https://ficheiros-web.xunta.gal/abertos/calendarios/calendario_laboral_2023.xlsx -o fuentes/galicia/2023.xlsx
curl -k --create-dirs https://ficheiros-web.xunta.gal/abertos/calendarios/calendario_laboral_2024.xlsx -o fuentes/galicia/2024.xlsx
curl -k --create-dirs https://ficheiros-web.xunta.gal/abertos/calendarios/calendario_laboral_2025.xlsx -o fuentes/galicia/2025.xlsx

curl -k --create-dirs https://opendata.euskadi.eus/contenidos/ds_eventos/calendario_laboral_2024/opendata/calendario_laboral_2024.xlsx -o fuentes/euskadi/2024.xlsx
curl -k --create-dirs https://opendata.euskadi.eus/contenidos/ds_eventos/calendario_laboral_2025/opendata/calendario_laboral_2025.xlsx -o fuentes/euskadi/2025.xlsx


# Generacion de ficheros .dat
mkdir -p ../datos/
mkdir -p ../models/
ln -s -r ./models/holiday.py ../models/holiday.py
python3 euskadi.py
python3 galicia.py

