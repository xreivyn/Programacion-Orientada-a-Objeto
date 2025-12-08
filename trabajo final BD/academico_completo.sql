-- 0. Borrar DB si existe (opcional, para pruebas limpias)
DROP DATABASE IF EXISTS gestion_academica;
-- 1. Crear la base de datos y usarla
CREATE DATABASE gestion_academica CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE gestion_academica;

-- 2. Tablas principales

CREATE TABLE Departamento (
    id_departamento INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Profesor (
    id_profesor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100),
    id_departamento INT,
    CONSTRAINT fk_prof_dept FOREIGN KEY (id_departamento)
        REFERENCES Departamento(id_departamento)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

CREATE TABLE Curso (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    creditos INT NOT NULL DEFAULT 3,
    id_departamento INT,
    CONSTRAINT fk_curso_dept FOREIGN KEY (id_departamento)
        REFERENCES Departamento(id_departamento)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

CREATE TABLE Clase (
    id_clase INT AUTO_INCREMENT PRIMARY KEY,
    id_curso INT NOT NULL,
    id_profesor INT,   -- permite NULL para ON DELETE SET NULL
    semestre VARCHAR(20) NOT NULL,
    horario VARCHAR(50),
    CONSTRAINT fk_clase_curso FOREIGN KEY (id_curso)
        REFERENCES Curso(id_curso)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_clase_prof FOREIGN KEY (id_profesor)
        REFERENCES Profesor(id_profesor)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);


CREATE TABLE Estudiante (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    matricula VARCHAR(20) UNIQUE NOT NULL,
    correo VARCHAR(100)
);

CREATE TABLE Inscripcion (
    id_inscripcion INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_clase INT NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT fk_insc_est FOREIGN KEY (id_estudiante)
        REFERENCES Estudiante(id_estudiante)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_insc_clase FOREIGN KEY (id_clase)
        REFERENCES Clase(id_clase)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    UNIQUE KEY uk_est_clase (id_estudiante, id_clase)
);


CREATE TABLE Calificacion (
    id_calificacion INT AUTO_INCREMENT PRIMARY KEY,
    id_inscripcion INT NOT NULL,
    tipo VARCHAR(50),
    nota DECIMAL(5,2),
    fecha DATE,
    CONSTRAINT fk_cal_ins FOREIGN KEY (id_inscripcion)
        REFERENCES Inscripcion(id_inscripcion)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

USE gestion_academica;

INSERT INTO Departamento (nombre) VALUES
('Ingenieria'), ('Ciencias'), ('Artes');

INSERT INTO Profesor (nombre, correo, id_departamento) VALUES
('Juan Perez', 'jperez@uni.edu', 1),
('Maria Lopez', 'mlopez@uni.edu', 2),
('Carlos Ruiz', 'cruiz@uni.edu', 1);

INSERT INTO Curso (nombre, creditos, id_departamento) VALUES
('Base de Datos', 4, 1),
('Matematica I', 3, 2),
('Historia del Arte', 2, 3);

INSERT INTO Clase (id_curso, id_profesor, semestre, horario) VALUES
(1, 1, '2025-1', 'Lun 8:00-10:00'),
(1, 3, '2025-1', 'Mie 10:00-12:00'),
(2, 2, '2025-1', 'Mar 9:00-11:00'),
(3, 2, '2025-1', 'Jue 14:00-16:00');

INSERT INTO Estudiante (nombre, matricula, correo) VALUES
('Kelvyn Vivas', '2025001', 'kelvyn@uni.edu'),
('Ana Torres', '2025002', 'ana@uni.edu'),
('Luis Gomez', '2025003', 'luis@uni.edu');

INSERT INTO Inscripcion (id_estudiante, id_clase, fecha) VALUES
(1, 1, '2025-01-15'),
(2, 1, '2025-01-16'),
(3, 2, '2025-01-17'),
(1, 3, '2025-01-15');

INSERT INTO Calificacion (id_inscripcion, tipo, nota, fecha) VALUES
(1, 'Examen 1', 85.50, '2025-02-10'),
(1, 'Examen Final', 90.00, '2025-05-15'),
(2, 'Examen 1', 78.00, '2025-02-10'),
(4, 'Examen 1', 88.00, '2025-02-11');
