#!/bin/bash

#GALICIA
mkdir -p fuentes/galicia
wget -nv https://ficheiros-web.xunta.gal/abertos/calendarios/calendario_laboral_2023.xlsx -O fuentes/galicia/2023.xlsx
wget -nv https://ficheiros-web.xunta.gal/abertos/calendarios/calendario_laboral_2024.xlsx -O fuentes/galicia/2024.xlsx
python3 galicia.py
