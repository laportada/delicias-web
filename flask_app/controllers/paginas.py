from flask import render_template
from flask_app import app

# --------- NUESTRA HISTORIA ---------
@app.route("/historia")
def historia():
    return render_template("historia.html")

# --------- EVENTOS Y CATERING ---------
@app.route("/eventos")
def eventos():
    return render_template("eventos.html")

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