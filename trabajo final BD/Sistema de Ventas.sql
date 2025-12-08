DROP DATABASE IF EXISTS ventas;
CREATE DATABASE ventas CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE ventas;

CREATE TABLE clientes (
  id_cliente INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(150) NOT NULL,
  correo VARCHAR(120),
  telefono VARCHAR(30),
  direccion VARCHAR(250)
);

CREATE TABLE productos (
  id_producto INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(150) NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  stock INT DEFAULT 0
);

-- Factura: cabecera
CREATE TABLE factura (
  id_factura INT AUTO_INCREMENT PRIMARY KEY,
  id_cliente INT,
  fecha DATE NOT NULL,
  total DECIMAL(12,2) DEFAULT 0,
  CONSTRAINT fk_fact_cliente FOREIGN KEY (id_cliente)
    REFERENCES clientes(id_cliente)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

-- Detalle: relación 1:N factura -> detalle (cada detalle un producto en la factura)
CREATE TABLE factura_detalle (
  id_detalle INT AUTO_INCREMENT PRIMARY KEY,
  id_factura INT NOT NULL,
  id_producto INT NOT NULL,
  cantidad INT NOT NULL,
  precio_unit DECIMAL(10,2) NOT NULL,
  CONSTRAINT fk_det_fact FOREIGN KEY (id_factura)
    REFERENCES factura(id_factura)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_det_prod FOREIGN KEY (id_producto)
    REFERENCES productos(id_producto)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

INSERT INTO clientes (nombre, correo, telefono, direccion) VALUES
('Empresa A', 'contacto@empresaa.com', '809-000-0000', 'Calle 1 #10'),
('Jose Perez', 'josep@correo.com', '809-111-1111', 'Av. Principal 45');

INSERT INTO productos (nombre, precio, stock) VALUES
('Laptop Modelo X', 750.00, 10),
('Mouse Óptico', 15.50, 100),
('Monitor 24"', 120.00, 20);

INSERT INTO factura (id_cliente, fecha, total) VALUES
(1, '2025-06-01', 0),
(2, '2025-06-02', 0);

INSERT INTO factura_detalle (id_factura, id_producto, cantidad, precio_unit) VALUES
(1, 1, 2, 750.00),  -- 2 laptops
(1, 2, 3, 15.50),   -- 3 mouses
(2, 3, 1, 120.00);  -- 1 monitor

-- a) Mostrar facturas con cliente y total calculado por join (suma del detalle)
SELECT f.id_factura, c.nombre AS cliente, f.fecha,
       SUM(d.cantidad * d.precio_unit) AS total_calculado
FROM factura f
LEFT JOIN clientes c ON f.id_cliente = c.id_cliente
LEFT JOIN factura_detalle d ON f.id_factura = d.id_factura
GROUP BY f.id_factura;

-- b) Actualizar total en la tabla factura (si quieres materializar)
UPDATE factura f
SET total = (
  SELECT IFNULL(SUM(d.cantidad * d.precio_unit),0)
  FROM factura_detalle d
  WHERE d.id_factura = f.id_factura
);

-- c) Productos con poco stock
SELECT nombre, stock FROM productos WHERE stock < 10;

-- d) Ventas por producto (cantidad vendida)
SELECT p.nombre, SUM(d.cantidad) AS total_vendido
FROM factura_detalle d
JOIN productos p ON d.id_producto = p.id_producto
GROUP BY p.id_producto;


-- CREATE CRUD ejemplos(nueva factura y detalle)
INSERT INTO factura (id_cliente, fecha) VALUES (1, '2025-07-01');
INSERT INTO factura_detalle (id_factura, id_producto, cantidad, precio_unit)
VALUES (LAST_INSERT_ID(), 2, 5, 15.50);

-- READ
SELECT * FROM factura WHERE id_factura = 1;
SELECT * FROM factura_detalle WHERE id_factura = 1;

-- UPDATE (cambiar precio unitario en detalle)
UPDATE factura_detalle SET precio_unit = 14.00 WHERE id_detalle = 2;

-- DELETE (borrar un detalle)
DELETE FROM factura_detalle WHERE id_detalle = 3;