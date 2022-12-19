# 1

from flask import Flask,render_template
# 1- Para programar el servidor tenemos que agregar un valor en el terminal en el  entorno virtual

# en mac: flask_app = hello.py
# En windows: set FLASK_APP = hello.PY

# 2- comando para ejecutar el servidor: 'flask --app hello run' en la terminal dentro del entorno virtual
# Comando para actualizar el servidor cada vez que se haga un cambio en el servidor : flask --app hello --debug run
# comando especial para lanzar el servidor en unpuerto diferente en el caso que el puerto 5000 este ocupado
# flask --app hello run -p 5001
# comando para cambiar el puerto : flask --app hello run -p 5001
# comando para lanzar en modo debug con puerto cambiado: flask --app hello --debug run -p 5001

app = Flask(__name__) # Para inicializar Flask, app sería nuestro servidor

@app.route("/hola") # Definimos la ruta donde vamos a ejecutar esta función
def hola_mundo(): # Retorna un str hola mundo flask
    return "Hola mundo Flask"

# Crear una ruta adios que retorne una despedida por ejemplo:hasta pronto

@app.route("/adios")
def despedidia():
    return "Hasta pronto see you later men"

# Ejemplo para enviar parametros por rutas

@app.route("/nombre/<name>")
def name(name):
    return f"Tu nombre es {name}"

# Realizar una ruta que devuelva el cuadrado de un número

@app.route("/operacion/<int:n>")
def cuadrado(n):
    return f"El cuadrado del número: {n} es {n * n}"

# Ejercicio realizar una ruta que dinamicamente pueda solicitar operaciones de suma ,resta,multiplicación y division
# operciones/10.5/0.5/suma    o culaquier operción que tenemos 
# segun los paramentros pasados en la url

@app.route('/operaciones/<float:n1>/<float:n2>/<ope>')
def calculadora(n1,n2,ope):
    if ope=="sum":
        return render_template("hola.html",resultado=f"La suma {n1} y {n2} es {n1+n2}")
    elif ope=="res":
        return render_template("hola.html",resultado=f"La resta de {n1} y {n2} es {n1-n2}")
    elif ope=="mult":
        return render_template("hola.html",resultado=f"La multiplicacion {n1} y {n2} es {n1*n2}")
    elif ope=="div":
        return render_template("hola.html",resultado=f"La division {n1} y {n2} es {n1/n2}") 
    
# Ejemplo de como devolver un html por flask

@app.route("/primerhtml/<nombre>")
def callhtml(nombre):
    return render_template(f"hola.html",name = nombre)
        




