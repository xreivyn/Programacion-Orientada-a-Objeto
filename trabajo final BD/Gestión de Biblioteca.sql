-- 1. Crear DB y usarla
DROP DATABASE IF EXISTS biblioteca;
CREATE DATABASE biblioteca CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE biblioteca;

-- 2. Tabla autores
CREATE TABLE autores (
  id_autor INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(150) NOT NULL,
  nacionalidad VARCHAR(80),
  fecha_nacimiento DATE
);

-- 3. Tabla libros
CREATE TABLE libros (
  id_libro INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(250) NOT NULL,
  id_autor INT,
  anio_publicacion YEAR,
  isbn VARCHAR(20) UNIQUE,
  stock INT DEFAULT 0,
  CONSTRAINT fk_libro_autor FOREIGN KEY (id_autor)
    REFERENCES autores(id_autor)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

INSERT INTO autores (nombre, nacionalidad, fecha_nacimiento) VALUES
('Gabriel García Márquez', 'Colombiana', '1927-03-06'),
('J. K. Rowling', 'Británica', '1965-07-31'),
('Jane Austen', 'Británica', '1775-12-16');

ALTER TABLE libros MODIFY anio_publicacion SMALLINT;

INSERT INTO libros (titulo, id_autor, anio_publicacion, isbn, stock) VALUES
('Cien años de soledad', 1, 1967, '9780307474728', 5),
('Harry Potter y la piedra filosofal', 2, 1997, '9780747532699', 12),
('Orgullo y prejuicio', 3, 1813, '9780141199078', 3);

-- a) Listar todos los libros
SELECT * FROM libros;

-- b) Mostrar libros con nombre del autor (JOIN)
SELECT l.titulo, a.nombre AS autor, l.anio_publicacion, l.stock
FROM libros l
LEFT JOIN autores a ON l.id_autor = a.id_autor;

-- c) Libros por autor
SELECT a.nombre, COUNT(l.id_libro) AS total_libros
FROM autores a
LEFT JOIN libros l ON a.id_autor = l.id_autor
GROUP BY a.id_autor;

-- d) Buscar por ISBN
SELECT * FROM libros WHERE isbn='9780747532699';

-- e) Libros con poco stock (ejemplo <5)
SELECT titulo, stock FROM libros WHERE stock < 5;

-- CREATE (nuevo libro)
INSERT INTO libros (titulo, id_autor, anio_publicacion, isbn, stock)
VALUES ('Nuevo Libro Ejemplo', 1, 2024, '1111111111111', 7);

-- READ
SELECT * FROM libros WHERE id_libro = 1;

-- UPDATE (actualizar stock)
UPDATE libros SET stock = stock + 5 WHERE id_libro = 1;

-- DELETE (eliminar autor - observa FK SET NULL)
DELETE FROM autores WHERE id_autor = 3;

