from flask import Flask
from flask_bcrypt import Bcrypt

# Instancia principal de Flask
app = Flask(__name__)
app.secret_key = "clave_secreta_delicias_2026"

# Bcrypt para encriptar contraseñas
bcrypt = Bcrypt(app)

# Importar controladores después de crear la app para evitar importaciones circulares
from flask_app.controllers import usuarios, productos, pedidos