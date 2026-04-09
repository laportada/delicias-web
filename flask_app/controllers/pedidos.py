from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.pedido import Pedido

# --------- FORMULARIO DELIVERY ---------
@app.route("/delivery")
def delivery():
    if "usuario_id" not in session:
        return redirect("/")
    return render_template("delivery.html")

# --------- CREAR PEDIDO ---------
@app.route("/pedido/crear", methods=["POST"])
def crear_pedido():
    if "usuario_id" not in session:
        return redirect("/")

    if not Pedido.validar_pedido(request.form):
        return redirect("/delivery")

    data = {
        "usuario_id": session["usuario_id"],
        "total": request.form["total"],
        "direccion": request.form["direccion"],
        "estado": "pendiente",
        "notas": request.form.get("notas", ""),
    }

    Pedido.guardar(data)
    return redirect("/mis_pedidos")

# --------- VER MIS PEDIDOS ---------
@app.route("/mis_pedidos")
def mis_pedidos():
    if "usuario_id" not in session:
        return redirect("/")
    
    pedidos = Pedido.get_por_usuario({"usuario_id": session["usuario_id"]})
    return render_template("mis_pedidos.html", pedidos=pedidos)