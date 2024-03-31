#!/bin/bash

# Descarga de CCAAs
mkdir -p fuentes/galicia
wget -nv https://ficheiros-web.xunta.gal/abertos/calendarios/calendario_laboral_2023.xlsx -O fuentes/galicia/2023.xlsx
wget -nv https://ficheiros-web.xunta.gal/abertos/calendarios/calendario_laboral_2024.xlsx -O fuentes/galicia/2024.xlsx
curl -k --create-dirs https://sede.asturias.es/documents/217768/291977/Calendario+festivos+Asturias.xlsx/6264daab-9417-f76a-c2f4-116f8f1810f9?t=1658389031223 -o fuentes/asturias/2024.xlsx

# Generacion de ficheros .dat
python3 asturias.py
python3 euskadi.py
python3 galicia.py

