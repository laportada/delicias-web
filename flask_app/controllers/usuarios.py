from flask import render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.models.usuario import Usuario

# --------- RUTA HOMEPAGE ---------
@app.route("/")
def index():
    return render_template("portada.html")

# --------- REGISTRO ---------
@app.route("/registro", methods=["POST"])
def registro():
    # 1. Validar datos
    if not Usuario.validar_registro(request.form):
        return redirect("/")

    # 2. Encriptar contraseña
    pw_hash = bcrypt.generate_password_hash(request.form["password"])

    # 3. Preparar datos
    data = {
        "nombre": request.form["nombre"],
        "email": request.form["email"],
        "password": pw_hash,
    }

    # 4. Guardar en BD
    nuevo_id = Usuario.guardar(data)

    # 5. Guardar en sesión
    session["usuario_id"] = nuevo_id
    session["nombre"] = request.form["nombre"]

    return redirect("/menu")

# --------- LOGIN ---------
@app.route("/login", methods=["POST"])
def login():
    usuario = Usuario.validar_login(request.form)
    if not usuario:
        return redirect("/")

    session["usuario_id"] = usuario.id
    session["nombre"] = usuario.nombre

    return redirect("/menu")

# --------- LOGOUT ---------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")