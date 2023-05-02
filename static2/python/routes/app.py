from flask import render_template, request, redirect, flash ,url_for
#import psycopg2
#import static2.python.controladores.login as c_login
#from static2.python.bd import obtener_conexion
from static2.python.bd import obtener_conexion
from __main__ import app


@app.route("/")
def index():
    return render_template('login/login.html')

@app.route('/login', methods= ["POST"])
def login():
        #if request.method == "POST":
            nombre = request.form["nombre"]
            clave = request.form["clave"]
            conexion = obtener_conexion().cursor()
            conexion.execute("SELECT * FROM usuario WHERE nombre = %s  AND clave = %s", (nombre,clave))
            usuario = conexion.fetchone()
            conexion.close()
            
            #user = c_login.inicio_ses(nombre,clave)
            if usuario is not None:
                return redirect(url_for('home'))
            else:
                flash("Usuario y contraseña no encontrados...")
                return render_template('login/login.html')
        #else:
            #return render_template('login/login.html')
        
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')