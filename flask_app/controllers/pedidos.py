from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.pedido import Pedido
from flask_app.models.usuario import Usuario
from flask_app.models.producto import Producto

# --------- FORMULARIO DELIVERY ---------
@app.route("/delivery", methods=["GET", "POST"])
def delivery():
    if request.method == "GET":
        productos = Producto.get_todos()
        return render_template("delivery.html", productos=productos)
    
    # POST: Crear pedido (sin login requerido)
    data = {
        "nombre": request.form.get("nombre"),
        "email": request.form.get("email"),
        "telefono": request.form.get("telefono"),
        "direccion": request.form.get("direccion"),
        "total": request.form.get("total"),
        "notas": request.form.get("notas", ""),
    }
    
    # Si hay usuario logeado, usar su data
    if session.get("usuario_id"):
        usuario = Usuario.get_por_id(session.get("usuario_id"))
        data["usuario_id"] = usuario["id"]
    else:
        # Para pedidos anónimos
        usuario_email = data.get("email")
        usuario = Usuario.get_por_email(usuario_email)
        if not usuario:
            # Crear usuario temporal
            usuario_data = {
                "nombre": data.get("nombre"),
                "email": usuario_email,
                "password": "delivery_" + usuario_email
            }
            Usuario.guardar(usuario_data)
            usuario = Usuario.get_por_email(usuario_email)
        data["usuario_id"] = usuario["id"]
    
    # Guardar pedido
    Pedido.guardar(data)
    flash("¡Pedido creado exitosamente! Nos pondremos en contacto pronto por WhatsApp.", "success")
    return redirect("/")

# --------- VER MIS PEDIDOS ---------
@app.route("/mis_pedidos")
def mis_pedidos():
    if "usuario_id" not in session:
        flash("Por favor inicia sesión para ver tus pedidos", "warning")
        return redirect("/")
    
    pedidos = Pedido.get_por_usuario({"usuario_id": session["usuario_id"]})
    return render_template("mis_pedidos.html", pedidos=pedidos)