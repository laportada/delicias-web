from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# Nombre de la base de datos
DB = "delicias_web"

class Producto:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.descripcion = data["descripcion"]
        self.precio = data["precio"]
        self.categoria = data["categoria"]
        self.disponible = data["disponible"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # --------- CREATE ---------
    @classmethod
    def guardar(cls, data):
        """Inserta un nuevo producto (menú) en la BD."""
        query = (
            "INSERT INTO productos (nombre, descripcion, precio, categoria, disponible) "
            "VALUES (%(nombre)s, %(descripcion)s, %(precio)s, %(categoria)s, %(disponible)s);"
        )
        return connectToMySQL(DB).query_db(query, data)

    # --------- READ ---------
    @classmethod
    def get_por_id(cls, data):
        """Busca un producto por id."""
        query = "SELECT * FROM productos WHERE id = %(id)s;"
        resultado = connectToMySQL(DB).query_db(query, data)
        if not resultado:
            return None
        return cls(resultado[0])

    @classmethod
    def get_todos(cls):
        """Obtiene todos los productos disponibles."""
        query = "SELECT * FROM productos WHERE disponible = 1 ORDER BY categoria, nombre;"
        resultados = connectToMySQL(DB).query_db(query)
        productos = []
        if resultados:
            for fila in resultados:
                productos.append(cls(fila))
        return productos

    @classmethod
    def get_por_categoria(cls, data):
        """Obtiene productos de una categoría específica."""
        query = "SELECT * FROM productos WHERE categoria = %(categoria)s AND disponible = 1 ORDER BY nombre;"
        resultados = connectToMySQL(DB).query_db(query, data)
        productos = []
        if resultados:
            for fila in resultados:
                productos.append(cls(fila))
        return productos

    # --------- UPDATE ---------
    @classmethod
    def actualizar(cls, data):
        """Actualiza un producto."""
        query = (
            "UPDATE productos "
            "SET nombre = %(nombre)s, descripcion = %(descripcion)s, precio = %(precio)s, "
            "categoria = %(categoria)s, disponible = %(disponible)s "
            "WHERE id = %(id)s;"
        )
        return connectToMySQL(DB).query_db(query, data)

    # --------- DELETE ---------
    @classmethod
    def eliminar(cls, data):
        """Marca un producto como no disponible (soft delete)."""
        query = "UPDATE productos SET disponible = 0 WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)

    # --------- VALIDACIONES ---------
    @staticmethod
    def validar_producto(form):
        """Valida los datos del formulario de producto."""
        es_valido = True
        nombre = form.get("nombre", "").strip()
        descripcion = form.get("descripcion", "").strip()
        precio = form.get("precio", "")
        categoria = form.get("categoria", "").strip()

        if len(nombre) < 2:
            flash("El nombre debe tener al menos 2 caracteres", "producto")
            es_valido = False

        if len(descripcion) < 3:
            flash("La descripción debe tener al menos 3 caracteres", "producto")
            es_valido = False

        try:
            p = float(precio)
            if p <= 0:
                flash("El precio debe ser mayor a 0", "producto")
                es_valido = False
        except ValueError:
            flash("El precio debe ser un número válido", "producto")
            es_valido = False

        if len(categoria) < 2:
            flash("Debes seleccionar una categoría válida", "producto")
            es_valido = False

        return es_valido