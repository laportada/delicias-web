# app/__init__.py
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Importar rutas después de crear la app para evitar importaciones circulares
from app import routes