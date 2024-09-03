# Flask Movie App

## Descripción

Este es el proyecto base en Python con Flask para MovieApp.

## Requerimientos

- Python 3.8
- pip

## Configuración

- Clonar el repositorio:

   git clone https://github.com/tu-usuario/FlaskMovieApp

- Crear un entorno virtual:

   python3 -m venv venv
   source venv/bin/activate

- Crear un archivo para las variables de entorno en la raiz del proyecto(donde guardaras tu clave de la API)

   .env, luego pip install python-dotenv para que lo puedas importar

## Instalación:
- Flask

   pip install flask

- Dependdencias 
   Luego de tener un entorno virtual activado y luego instala las dependencias requeridas con:

      pip freeze > requirements.txt o python3 -m pip freeze > requirements.txt 

   Y para que solo muestre las que tu instalaste en caso de que ya venga con otras dependencias:

      pip install pipreqs o python3 -m pip install pipreqs

## Estructura del proyecto**

    - `app.py`: Archivo principal de la aplicación Flask.
    - `config.py`: Configuración de la aplicación, cargada desde el archivo `.env`.
    - `app/routes.py`: Define las rutas y la lógica de la aplicación.
    - `app/models.py` : Define los modelos de datos utilizados en la aplicación.

## Ejecutar la aplicación

Para ejecutar la aplicación

    python app.py o python3 app.py
