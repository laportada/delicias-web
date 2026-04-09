from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import date

# Nombre de la base de datos
DB = "delicias_web"

class Pedido:
    def __init__(self, data):
        self.id = data["id"]
        self.usuario_id = data["usuario_id"]
        self.total = data["total"]
        self.direccion = data["direccion"]
        self.estado = data["estado"]  # pendiente, confirmado, entregado, cancelado
        self.notas = data.get("notas", "")
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # --------- CREATE ---------
    @classmethod
    def guardar(cls, data):
        """Crea un nuevo pedido/delivery."""
        query = (
            "INSERT INTO pedidos (usuario_id, total, direccion, estado, notas) "
            "VALUES (%(usuario_id)s, %(total)s, %(direccion)s, %(estado)s, %(notas)s);"
        )
        return connectToMySQL(DB).query_db(query, data)

    # --------- READ ---------
    @classmethod
    def get_por_id(cls, data):
        """Busca un pedido por id."""
        query = "SELECT * FROM pedidos WHERE id = %(id)s;"
        resultado = connectToMySQL(DB).query_db(query, data)
        if not resultado:
            return None
        return cls(resultado[0])

    @classmethod
    def get_por_usuario(cls, data):
        """Obtiene todos los pedidos de un usuario."""
        query = "SELECT * FROM pedidos WHERE usuario_id = %(usuario_id)s ORDER BY created_at DESC;"
        resultados = connectToMySQL(DB).query_db(query, data)
        pedidos = []
        if resultados:
            for fila in resultados:
                pedidos.append(cls(fila))
        return pedidos

    # --------- UPDATE ---------
    @classmethod
    def actualizar_estado(cls, data):
        """Actualiza el estado de un pedido."""
        query = "UPDATE pedidos SET estado = %(estado)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)

    # --------- VALIDACIONES ---------
    @staticmethod
    def validar_pedido(form):
        """Valida los datos del formulario de pedido."""
        es_valido = True
        direccion = form.get("direccion", "").strip()
        total = form.get("total", "")

        if len(direccion) < 5:
            flash("La dirección debe tener al menos 5 caracteres", "pedido")
            es_valido = False

        try:
            t = float(total)
            if t <= 0:
                flash("El total debe ser mayor a 0", "pedido")
                es_valido = False
        except ValueError:
            flash("El total debe ser un número válido", "pedido")
            es_valido = False

        return es_valido