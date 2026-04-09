# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu_clave_secreta_aqui'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:password@localhost/delicias_web'
    SQLALCHEMY_TRACK_MODIFICATIONS = False