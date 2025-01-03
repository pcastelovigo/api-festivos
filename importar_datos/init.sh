#!/bin/bash
cd "$(dirname "$0")"

# Descarga de CCAAs
curl -k --create-dirs https://ficheiros-web.xunta.gal/abertos/calendarios/calendario_laboral_2023.xlsx -o fuentes/galicia/2023.xlsx
curl -k --create-dirs https://ficheiros-web.xunta.gal/abertos/calendarios/calendario_laboral_2024.xlsx -o fuentes/galicia/2024.xlsx
curl -k --create-dirs https://ficheiros-web.xunta.gal/abertos/calendarios/calendario_laboral_2025.xlsx -o fuentes/galicia/2025.xlsx
#curl -k --create-dirs https://sede.asturias.es/documents/217768/291977/Calendario+festivos+Asturias.xlsx/6264daab-9417-f76a-c2f4-116f8f1810f9?t=1658389031223 -o fuentes/asturias/2024.xlsx
curl -k --create-dirs https://opendata.euskadi.eus/contenidos/ds_eventos/calendario_laboral_2024/opendata/calendario_laboral_2024.xlsx -o fuentes/euskadi/2024.xlsx
#curl -k --create-dirs https://www.juntadeandalucia.es/datosabiertos/portal/dataset/12ea04e9-0a43-45c0-b31d-02763ee53feb/resource/c74d0d5e-15e2-48f3-a107-3f3babcee085/download/calendario_locales_2024.xls -o fuentes/andalucia/2024.xls
curl -k --create-dirs https://analisi.transparenciacatalunya.cat/api/views/b4eh-r8up/rows.csv?accessType=DOWNLOAD -o fuentes/catalunya/2024.csv


# Generacion de ficheros .dat
mkdir -p ../datos/
mkdir -p ../models/
ln -s -r ./models/holiday.py ../models/holiday.py
#python3 asturias.py
python3 euskadi.py
python3 galicia.py
#python3 andalucia.py
python3 catalunya.py

