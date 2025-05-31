# api-festivos

Requisitos:

    · Instalar dependencias => pip install -r requirements.txt

Para descargar los datos y lanzar:

    ./importar_datos/init.sh

    uvicorn main:app --reload

Obtener datos de la api:

    127.0.0.1:8000/año/estado/region/localidad

Ejemplo

    127.0.0.1:8000/2024/es/gl/a-coruna

![imagen](https://github.com/pcastelovigo/api-festivos/assets/20586382/e0a4b21d-67be-4000-9c62-5c9737efa709)


En las rutas no hay acentos ni dieresis, "ñ" es "n", "ç" es "c", espacios son guiones y puntos guiones bajos.


# Cobertura

A fecha de 31/05/2025 tiene los datos locales para Galicia y autonómicos para el resto de España

Los datos locales deben ser obtenidos cada año de las listas publicadas por cada comunidad autonoma, puesto que los ayuntamientos tienen la potestad de marcar sus propios festivos y cambiarlos cada año


# Contribuir

Las comunidades sacan las listas de festivos en diversos formatos: excel, csv, ficheros de texto, JSON...

Normalmente a finales de año dan la lista para el año siguiente. Muchos se publican en https://datos.gob.es/es/

Si haces un PR para la carpeta importar_datos será muy bienvenido.
