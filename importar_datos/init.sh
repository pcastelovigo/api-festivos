#!/bin/bash

#GALICIA
mkdir -p fuentes/galicia
wget -N -nv https://ficheiros-web.xunta.gal/abertos/calendarios/calendario_laboral_2023.xlsx -P fuentes/galicia
wget -N -nv https://ficheiros-web.xunta.gal/abertos/calendarios/calendario_laboral_2024.xlsx -P fuentes/galicia
python3 galicia.py
