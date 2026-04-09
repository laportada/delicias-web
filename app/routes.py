# app/routes.py
from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/horarios')
def horarios():
    return render_template('horarios.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.route('/delivery')
def delivery():
    return render_template('delivery.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')