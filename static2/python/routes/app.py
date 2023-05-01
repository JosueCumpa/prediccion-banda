from flask import render_template, request, redirect, flash ,url_for
import psycopg2
import static2.python.controladores.login as c_login
from __main__ import app


@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route('/login', methods= ["GET","POST"])
def login():
        if request.method == "POST":
            nombre = request.form["nombre"]
            clave = request.form["clave"]
            user = c_login.inicio_ses(nombre,clave)
            if user != None:
                redirect(url_for('home'))
            else:
                flash("Usuario y contraseña no encontrados...")
                return render_template('login/login.html')
        else:
            return render_template('login/login.html')
        
@app.route('/home')
def home():
    return render_template('home.html')