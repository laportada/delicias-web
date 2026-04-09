from flask import render_template
from flask_app import app

# --------- PÁGINA PRINCIPAL ---------
@app.route("/home")
def home():
    return render_template("home.html")

# --------- QUIÉNES SOMOS ---------
@app.route("/quienes_somos")
def quienes_somos():
    return render_template("quienes_somos.html")

# --------- HORARIOS ---------
@app.route("/horarios")
def horarios():
    return render_template("horarios.html")

# --------- GALERÍA ---------
@app.route("/galeria")
def galeria():
    return render_template("galeria.html")

# --------- CONTACTO ---------
@app.route("/contacto")
def contacto():
    return render_template("contacto.html")