# Delicias Web - Cafetería Online 🍰☕

Aplicación web profesional para una cafetería, construida con Flask y MySQL. Incluye sistema de autenticación, catálogo de productos dinámico y gestión de pedidos de delivery.

## 🎯 Características

- ✅ **Autenticación segura**: Registro e login con contraseñas encriptadas (bcrypt)
- ✅ **Catálogo dinámico**: Menú de productos organizados por categoría
- ✅ **Sistema de pedidos**: Delivery con historial de compras
- ✅ **Diseño responsivo**: Compatible con mobile y desktop
- ✅ **Arquitectura profesional**: Patrón MVC con separación clara de responsabilidades

## 🏗️ Estructura del Proyecto

```
delicias-web/
├── flask_app/
│   ├── __init__.py                 # Inicialización Flask + bcrypt
│   ├── config/
│   │   ├── __init__.py
│   │   └── mysqlconnection.py      # Conexión a BD (MySQL)
│   ├── models/
│   │   ├── usuario.py              # Modelo Usuario (login/registro)
│   │   ├── producto.py             # Modelo Producto (menú)
│   │   ├── pedido.py               # Modelo Pedido (delivery)
│   │   └── __init__.py
│   ├── controllers/
│   │   ├── usuarios.py             # Rutas: auth
│   │   ├── productos.py            # Rutas: menú
│   │   ├── pedidos.py              # Rutas: delivery
│   │   ├── paginas.py              # Rutas: páginas estáticas
│   │   └── __init__.py
│   ├── templates/                  # Plantillas HTML (Jinja2)
│   │   ├── base.html               # Plantilla base
│   │   ├── index.html              # Login/Registro
│   │   ├── home.html               # Página principal
│   │   ├── menu.html               # Catálogo
│   │   ├── producto_detalle.html   # Detalle de producto
│   │   ├── delivery.html           # Formulario pedido
│   │   ├── mis_pedidos.html        # Historial
│   │   ├── quienes_somos.html
│   │   ├── horarios.html
│   │   ├── galeria.html
│   │   └── contacto.html
│   └── static/
│       ├── css/styles.css          # Estilos principales
│       ├── js/scripts.js           # JavaScript
│       └── images/logo.jpg         # Logo
├── database.sql                    # Script para crear BD
├── DATABASE_SETUP.md               # Instrucciones BD
├── run.py                          # Punto de entrada
├── requirements.txt                # Dependencias
└── .gitignore
```

## 🚀 Inicio Rápido

### 1. Clonar el Repositorio
```bash
git clone https://github.com/laportada/delicias-web.git
cd delicias-web
```

### 2. Configurar Entorno Virtual (opcional pero recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos
```bash
# Lee las instrucciones en DATABASE_SETUP.md
mysql -u root -p < database.sql
```

### 5. Ejecutar la Aplicación
```bash
python run.py
```

Accede a: `http://localhost:5000`

## 📚 Tecnologías Utilizadas

- **Backend**: Flask 3.1.2, Python 3.x
- **Base de Datos**: MySQL + PyMySQL
- **Seguridad**: Flask-Bcrypt
- **Frontend**: HTML5, CSS3, Jinja2
- **Control de versiones**: Git

## 🔐 Seguridad

- ✅ Contraseñas encriptadas con bcrypt
- ✅ Protección contra SQL injection (parámetros seguros)
- ✅ Sesiones seguras con Flask
- ✅ Validación en servidor y cliente

## 📖 Rutas Disponibles

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Login/Registro |
| `/home` | GET | Página principal |
| `/menu` | GET | Catálogo de productos |
| `/producto/<id>` | GET | Detalle de producto |
| `/delivery` | GET | Formulario de pedido |
| `/pedido/crear` | POST | Crear pedido |
| `/mis_pedidos` | GET | Historial de pedidos |
| `/registro` | POST | Registrar usuario |
| `/login` | POST | Iniciar sesión |
| `/logout` | GET | Cerrar sesión |
| `/quienes_somos` | GET | Información |
| `/horarios` | GET | Horarios |
| `/galeria` | GET | Galería |
| `/contacto` | GET | Contacto |

## 🎨 Paleta de Colores

- **Primario**: `#8b4513` (Café oscuro)
- **Secundario**: `#d4a574` (Crema café)
- **Fondo**: `#f9f5f0` (Crema clara)
- **Texto**: `#333` (Gris oscuro)

## 📝 Validaciones Implementadas

### Usuarios
- Nombre: mínimo 2 caracteres
- Email: formato válido, sin duplicados
- Contraseña: mínimo 8 caracteres, confirmación

### Productos
- Nombre: mínimo 2 caracteres
- Descripción: mínimo 3 caracteres
- Precio: mayor a 0
- Categoría: válida

### Pedidos
- Dirección: mínimo 5 caracteres
- Total: mayor a 0

## 🔧 Configuración Personalizada

### Cambiar Usuario/Contraseña MySQL
Edita `flask_app/config/mysqlconnection.py`:
```python
user='tu_usuario',
password='tu_contraseña',
```

### Cambiar Puerto Flask
En `run.py`:
```python
app.run(debug=True, port=5000)  # Cambia el puerto aquí
```

## 📦 Dependencias

```
bcrypt==5.0.0
Flask==3.1.2
Flask-Bcrypt==1.0.1
PyMySQL==1.1.2
Jinja2==3.1.6
Werkzeug==3.1.3
```

## 🐛 Solución de Problemas

### Error: "Access denied for user 'root'@'localhost'"
- Verifica que MySQL esté ejecutándose
- Cambia usuario/contraseña en `mysqlconnection.py`

### Error: "No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Error: "Unknown database 'delicias_web'"
```bash
mysql -u root -p < database.sql
```

## 👨‍💻 Autor

Desarrollado como parte del aprendizaje de Flask y arquitectura profesional.

## 📄 Licencia

Este proyecto es de código abierto.

## 🌐 Repositorio

[GitHub - laportada/delicias-web](https://github.com/laportada/delicias-web)