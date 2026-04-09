from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.producto import Producto

# --------- MENÚ (Mostrar todos los productos) ---------
@app.route("/menu")
def menu():
    productos = Producto.get_todos()
    return render_template("menu.html", productos=productos)

# --------- MENÚ POR CATEGORÍA ---------
@app.route("/menu/<categoria>")
def menu_por_categoria(categoria):
    productos = Producto.get_por_categoria({"categoria": categoria})
    return render_template("menu.html", productos=productos, categoria=categoria)

# --------- VER DETALLE DE PRODUCTO ---------
@app.route("/producto/<int:id>")
def ver_producto(id):
    producto = Producto.get_por_id({"id": id})
    if not producto:
        return redirect("/menu")
    return render_template("producto_detalle.html", producto=producto)