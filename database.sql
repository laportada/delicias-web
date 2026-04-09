-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS delicias_web;
USE delicias_web;

-- Tabla de Usuarios (clientes)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla de Productos (Menú)
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    disponible BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla de Pedidos (Delivery)
CREATE TABLE IF NOT EXISTS pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    direccion TEXT NOT NULL,
    estado ENUM('pendiente', 'confirmado', 'entregado', 'cancelado') DEFAULT 'pendiente',
    notas TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla intermedia Detalles de Pedidos (qué productos en cada pedido)
CREATE TABLE IF NOT EXISTS detalles_pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL DEFAULT 1,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insertar productos de ejemplo
INSERT INTO productos (nombre, descripcion, precio, categoria, disponible) VALUES
('Espresso', 'Café espresso puro, fuerte y concentrado', 2.50, 'Cafés', 1),
('Cappuccino', 'Espresso con leche vaporizada y espuma ligera', 3.50, 'Cafés', 1),
('Latte', 'Espresso suave con abundante leche caliente', 4.00, 'Cafés', 1),
('Mocha', 'Espresso con chocolate y leche espumada', 4.50, 'Cafés', 1),
('Tarta de Chocolate', 'Deliciosa tarta casera de chocolate oscuro', 5.00, 'Pasteles', 1),
('Croissant', 'Croissant francés recién hecho', 2.00, 'Pasteles', 1),
('Muffin de Arándanos', 'Muffin esponjoso con arándanos frescos', 3.00, 'Pasteles', 1),
('Galleta con Chispas', 'Galleta casera con chispas de chocolate', 1.50, 'Pasteles', 1);

-- Índices para mejorar rendimiento
CREATE INDEX idx_usuarios_email ON usuarios(email);
CREATE INDEX idx_pedidos_usuario ON pedidos(usuario_id);
CREATE INDEX idx_productos_categoria ON productos(categoria);
CREATE INDEX idx_detalles_pedido ON detalles_pedidos(pedido_id);
CREATE INDEX idx_detalles_producto ON detalles_pedidos(producto_id);