from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import bcrypt

# Nombre de la base de datos
DB = "delicias_web"

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # --------- CREATE ---------
    @classmethod
    def guardar(cls, data):
        """Inserta un nuevo usuario (cliente) en la BD."""
        query = (
            "INSERT INTO usuarios (nombre, email, password) "
            "VALUES (%(nombre)s, %(email)s, %(password)s);"
        )
        return connectToMySQL(DB).query_db(query, data)

    # --------- READ ---------
    @classmethod
    def get_por_email(cls, data):
        """Busca un usuario por email."""
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultado = connectToMySQL(DB).query_db(query, data)
        if not resultado:
            return None
        return cls(resultado[0])

    @classmethod
    def get_por_id(cls, data):
        """Busca un usuario por id."""
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultado = connectToMySQL(DB).query_db(query, data)
        if not resultado:
            return None
        return cls(resultado[0])

    # --------- VALIDACIONES ---------
    @staticmethod
    def validar_registro(form):
        """Valida los datos del formulario de registro."""
        es_valido = True
        nombre = form.get("nombre", "").strip()
        email = form.get("email", "").strip()
        password = form.get("password", "")
        confirm = form.get("confirm_password", "")

        if len(nombre) < 2:
            flash("El nombre debe tener al menos 2 caracteres", "register")
            es_valido = False

        if "@" not in email or "." not in email:
            flash("E-mail no tiene un formato válido", "register")
            es_valido = False
        else:
            usuario = Usuario.get_por_email({"email": email})
            if usuario:
                flash("El e-mail ya está registrado", "register")
                es_valido = False

        if len(password) < 8:
            flash("La contraseña debe tener al menos 8 caracteres", "register")
            es_valido = False

        if password != confirm:
            flash("La contraseña y la confirmación no coinciden", "register")
            es_valido = False

        return es_valido

    @staticmethod
    def validar_login(form):
        """Valida los datos del login."""
        email = form.get("email", "").strip()
        password = form.get("password", "")

        usuario_en_bd = Usuario.get_por_email({"email": email})

        if not usuario_en_bd:
            flash("E-mail no está registrado", "login")
            return False

        if not bcrypt.check_password_hash(usuario_en_bd.password, password):
            flash("Contraseña incorrecta", "login")
            return False

        return usuario_en_bd