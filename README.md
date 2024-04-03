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
