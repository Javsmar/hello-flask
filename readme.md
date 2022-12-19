# Aplicación para introducción a Flask

programa echo en python con el framework Flask, Hello world

# Instalación

En su esntrono ejecutar el comando
```
pip install -r requirements.txt
```
Las librerias utilizada flask https://flask.palletsprojects.com/en/2.2.x/

# Ejecución del programa

1- Para programar el servidor tenemos que agregar un valor en el terminal en el  entorno virtual

- en mac: flask_app = hello.py
- En windows: set FLASK_APP = hello.PY

2- comando para ejecutar el servidor: 
flask --app hello run 

- Comando para actualizar el servidor cada vez que se haga un cambio en el servidor : flask --app hello --debug run
- comando especial para lanzar el servidor en unpuerto diferente en el caso que el puerto 5000 este ocupado
- flask --app hello run -p 5001
- comando para cambiar el puerto : flask --app hello run -p 5001
- comando para lanzar en modo debug con puerto cambiado: flask --app hello --debug run -p 5001
