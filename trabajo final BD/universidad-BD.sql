-- ============================
--   BASE DE DATOS UNIVERSIDAD
-- ============================
CREATE DATABASE IF NOT EXISTS universidad;
USE universidad;

-- ============================
-- TABLA DEPARTAMENTO
-- ============================
CREATE TABLE Departamento (
    DepartamentoID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL
);

INSERT INTO Departamento (Nombre) VALUES
('Ingeniería'),
('Administración'),
('Artes'),
('Salud'),
('Educación');

-- ============================
-- TABLA ESTUDIANTE
-- ============================
CREATE TABLE Estudiante (
    EstudianteID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    FechaNacimiento DATE NOT NULL,
    DepartamentoID INT,
    FOREIGN KEY (DepartamentoID) REFERENCES Departamento(DepartamentoID)
);

INSERT INTO Estudiante (Nombre, Apellido, FechaNacimiento, DepartamentoID) VALUES
('Ana', 'García', '2001-05-12', 1),
('Luis', 'Pérez', '2000-11-30', 2),
('María', 'López', '1999-03-22', 1),
('Carlos', 'Gómez', '2002-07-18', 3),
('Andrea', 'Santos', '2001-01-10', 4),
('Pedro', 'Ramírez', '1998-09-02', 1),
('Laura', 'García', '2000-02-14', 5),
('Jorge', 'Martínez', '1999-12-01', 2),
('Daniela', 'Torres', '2001-09-25', 3),
('Kevin', 'Rojas', '1998-04-08', 1);

-- ============================
-- TABLA PROFESOR
-- ============================
CREATE TABLE Profesor (
    ProfesorID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    DepartamentoID INT,
    FOREIGN KEY (DepartamentoID) REFERENCES Departamento(DepartamentoID)
);

INSERT INTO Profesor (Nombre, Apellido, DepartamentoID) VALUES
('Roberto', 'Fernández', 1),
('Elena', 'Morales', 2),
('Sofía', 'Jiménez', 3),
('Mario', 'Toribio', 4),
('Lucía', 'Hernández', 1);

-- ============================
-- TABLA CURSO
-- ============================
CREATE TABLE Curso (
    CursoID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Creditos INT NOT NULL,
    DepartamentoID INT,
    FOREIGN KEY (DepartamentoID) REFERENCES Departamento(DepartamentoID)
);

INSERT INTO Curso (Nombre, Creditos, DepartamentoID) VALUES
('Programación I', 4, 1),
('Estructura de Datos', 4, 1),
('Contabilidad', 3, 2),
('Marketing', 3, 2),
('Pintura Básica', 2, 3),
('Anatomía', 4, 4);

-- ============================
-- TABLA CLASE
-- ============================
CREATE TABLE Clase (
    ClaseID INT PRIMARY KEY AUTO_INCREMENT,
    CursoID INT,
    ProfesorID INT,
    Semestre VARCHAR(10),
    FOREIGN KEY (CursoID) REFERENCES Curso(CursoID),
    FOREIGN KEY (ProfesorID) REFERENCES Profesor(ProfesorID)
);

INSERT INTO Clase (CursoID, ProfesorID, Semestre) VALUES
(1, 1, '2024-1'),
(2, 5, '2024-1'),
(3, 2, '2024-1'),
(4, 2, '2024-2'),
(5, 3, '2024-2'),
(6, 4, '2024-2');

-- ============================
-- TABLA INSCRIPCION
-- ============================
CREATE TABLE Inscripcion (
    InscripcionID INT PRIMARY KEY AUTO_INCREMENT,
    EstudianteID INT,
    ClaseID INT,
    FechaInscripcion DATE NOT NULL,
    UNIQUE (EstudianteID, ClaseID),
    FOREIGN KEY (EstudianteID) REFERENCES Estudiante(EstudianteID),
    FOREIGN KEY (ClaseID) REFERENCES Clase(ClaseID)
);

INSERT INTO Inscripcion (EstudianteID, ClaseID, FechaInscripcion) VALUES
(1,1,'2024-01-15'),
(2,1,'2024-01-16'),
(3,2,'2024-01-17'),
(4,3,'2024-01-18'),
(5,4,'2024-01-19'),
(6,5,'2024-01-21'),
(7,6,'2024-01-22'),
(8,1,'2024-01-23'),
(9,3,'2024-01-24'),
(10,2,'2024-01-25');

-- ============================
-- TABLA CALIFICACION
-- ============================
CREATE TABLE Calificacion (
    CalificacionID INT PRIMARY KEY AUTO_INCREMENT,
    InscripcionID INT NOT NULL,
    Nota DECIMAL(4,2) CHECK (Nota >= 0 AND Nota <= 100),
    FechaRegistro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (InscripcionID) REFERENCES Inscripcion(InscripcionID)
);

INSERT INTO Calificacion (InscripcionID, Nota) VALUES
(1, 88.50),
(2, 90.00),
(3, 75.25),
(4, 95.00),
(5, 60.00),
(6, 85.75),
(7, 92.50),
(8, 78.00),
(9, 88.00),
(10, 99.00);
