import os
from flask import Flask
from flask_bcrypt import Bcrypt

# Obtener la ruta del directorio actual de flask_app
basedir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(basedir)

# Instancia principal de Flask con rutas corregidas
app = Flask(__name__, 
            template_folder=os.path.join(parent_dir, 'templates'),
            static_folder=os.path.join(parent_dir, 'static'))

app.secret_key = "clave_secreta_delicias_2026"

# Bcrypt para encriptar contraseñas
bcrypt = Bcrypt(app)

# Importar controladores después de crear la app para evitar importaciones circulares
from flask_app.controllers import usuarios, productos, pedidos