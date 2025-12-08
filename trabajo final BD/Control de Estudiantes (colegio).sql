DROP DATABASE IF EXISTS colegio;
CREATE DATABASE colegio CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE colegio;

CREATE TABLE estudiantes (
  id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(150) NOT NULL,
  matricula VARCHAR(30) UNIQUE NOT NULL,
  fecha_ingreso DATE
);

CREATE TABLE cursos (
  id_curso INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(150) NOT NULL,
  grado INT
);

-- Matriculas: relación N:M estudiantes <-> cursos
CREATE TABLE matriculas (
  id_matricula INT AUTO_INCREMENT PRIMARY KEY,
  id_estudiante INT NOT NULL,
  id_curso INT NOT NULL,
  fecha DATE NOT NULL,
  CONSTRAINT fk_mat_est FOREIGN KEY (id_estudiante)
    REFERENCES estudiantes(id_estudiante)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_mat_curso FOREIGN KEY (id_curso)
    REFERENCES cursos(id_curso)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  UNIQUE KEY uk_est_curso (id_estudiante, id_curso)
);

INSERT INTO estudiantes (nombre, matricula, fecha_ingreso) VALUES
('Lucia Martinez', '2024001', '2024-08-15'),
('Pedro Alvarez', '2024002', '2024-08-15'),
('Sofia Díaz', '2024003', '2024-08-16');

INSERT INTO cursos (nombre, grado) VALUES
('Matemáticas Básicas', 1),
('Ciencias Naturales', 1),
('Inglés Básico', 1);

INSERT INTO matriculas (id_estudiante, id_curso, fecha) VALUES
(1, 1, '2024-09-01'),
(2, 1, '2024-09-01'),
(3, 2, '2024-09-02'),
(1, 3, '2024-09-03');

--- Consultas (SELECT y JOIN)
-- a) Listar alumnos en cada curso
SELECT c.nombre AS curso, e.nombre AS estudiante, m.fecha
FROM matriculas m
JOIN estudiantes e ON m.id_estudiante = e.id_estudiante
JOIN cursos c ON m.id_curso = c.id_curso
ORDER BY c.id_curso;

-- b) Cursos por estudiante
SELECT e.nombre AS estudiante, GROUP_CONCAT(c.nombre SEPARATOR ', ') AS cursos
FROM estudiantes e
LEFT JOIN matriculas m ON e.id_estudiante = m.id_estudiante
LEFT JOIN cursos c ON m.id_curso = c.id_curso
GROUP BY e.id_estudiante;

-- c) Conteo de estudiantes por curso
SELECT c.nombre, COUNT(m.id_estudiante) AS cantidad
FROM cursos c
LEFT JOIN matriculas m ON c.id_curso = m.id_curso
GROUP BY c.id_curso;

--- CRUD ejemplos
-- CREATE (nueva matricula)
INSERT INTO matriculas (id_estudiante, id_curso, fecha) VALUES (2, 3, '2024-10-01');

-- READ
SELECT * FROM matriculas WHERE id_matricula = 1;

-- UPDATE (cambiar curso)
UPDATE matriculas SET id_curso = 2 WHERE id_matricula = 1;

-- DELETE (anular matricula)
DELETE FROM matriculas WHERE id_matricula = 2;