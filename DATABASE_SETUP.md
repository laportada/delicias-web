# Configuración de Base de Datos para Delicias Web

## 📋 Prerequisitos

- MySQL Server instalado y ejecutándose
- Usuario MySQL (por defecto: `root` con contraseña `root`)
- Cliente MySQL o herramienta como MySQL Workbench

## 🗄️ Pasos para Configurar la Base de Datos

### 1. Abrir MySQL
```bash
mysql -u root -p
# Te pedirá la contraseña (por defecto: root)
```

### 2. Ejecutar el Script SQL
Tienes dos opciones:

**Opción A: Desde la línea de comandos**
```bash
mysql -u root -p < database.sql
```

**Opción B: Desde MySQL CLI**
```sql
source database.sql;
-- O copiar y pegar el contenido de database.sql
```

### 3. Verificar la Instalación
```sql
USE delicias_web;
SHOW TABLES;
```

Deberías ver:
- `usuarios`
- `productos`
- `pedidos`
- `detalles_pedidos`

### 4. Ver los productos de ejemplo
```sql
SELECT * FROM productos;
```

## ⚙️ Configuración de Conexión

Si tu usuario MySQL es diferente, edita `flask_app/config/mysqlconnection.py`:

```python
connection = pymysql.connect(
    host='localhost',
    user='tu_usuario',      # Cambia aquí
    password='tu_contraseña',  # Cambia aquí
    db=db,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True,
)
```

## 📊 Estructura de Tablas

### `usuarios`
- Clientes registrados
- Email único para login
- Contraseña encriptada con bcrypt

### `productos`
- Menú de la cafetería
- Organizado por categoría (Cafés, Pasteles)
- Campo disponible para habilitar/deshabilitar

### `pedidos`
- Pedidos de delivery realizados
- Estados: pendiente, confirmado, entregado, cancelado
- Vinculado con usuario

### `detalles_pedidos`
- Productos en cada pedido
- Cantidad y precio unitario registrado
- Permite histórico de precios

## ✅ Listo!

La base de datos está configurada. Ahora puedes ejecutar:
```bash
python run.py
```

¡La aplicación estará lista en `http://localhost:5000`!