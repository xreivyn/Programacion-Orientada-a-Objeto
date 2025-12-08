-- 1. Todos los estudiantes
SELECT * FROM Estudiante;

-- 2. Solo nombres y apellidos
SELECT Nombre, Apellido FROM Estudiante;

-- 3. Estudiantes de un departamento (ejemplo DepartamentoID=1)
SELECT * FROM Estudiante
WHERE DepartamentoID = 1;

-- 4. Ordenados por fecha de nacimiento (viejos primero)
SELECT * FROM Estudiante
ORDER BY FechaNacimiento ASC;

-- 5. Cantidad de estudiantes
SELECT COUNT(*) AS TotalEstudiantes FROM Estudiante;

-- 6. Apellido García
SELECT * FROM Estudiante WHERE Apellido = 'García';

-- 7. Nombres que empiezan con A
SELECT * FROM Estudiante WHERE Nombre LIKE 'A%';

-- 8. Join estudiante + departamento
SELECT e.Nombre, e.Apellido, d.Nombre AS Departamento
FROM Estudiante e
JOIN Departamento d ON e.DepartamentoID = d.DepartamentoID;

-- 9. Promedio de calificaciones por estudiante
SELECT e.Nombre, e.Apellido,
       AVG(c.Nota) AS Promedio
FROM Calificacion c
JOIN Inscripcion i ON c.InscripcionID = i.InscripcionID
JOIN Estudiante e ON e.EstudianteID = i.EstudianteID
GROUP BY e.EstudianteID;

-- 10. Cantidad de estudiantes por departamento
SELECT d.Nombre, COUNT(e.EstudianteID) AS Total
FROM Departamento d
LEFT JOIN Estudiante e ON d.DepartamentoID = e.DepartamentoID
GROUP BY d.DepartamentoID;

-- 11. Cursos impartidos por cada profesor
SELECT p.Nombre, p.Apellido, COUNT(c.ClaseID) AS CursosImpartidos
FROM Profesor p
LEFT JOIN Clase c ON p.ProfesorID = c.ProfesorID
GROUP BY p.ProfesorID;

-- 12. Estudiantes con promedio mayor a 90
SELECT e.Nombre, e.Apellido, AVG(c.Nota) AS Promedio
FROM Calificacion c
JOIN Inscripcion i ON c.InscripcionID = i.InscripcionID
JOIN Estudiante e ON e.EstudianteID = i.EstudianteID
GROUP BY e.EstudianteID
HAVING Promedio > 90;

-- 13. Top 5 estudiantes con mejores promedios
SELECT e.Nombre, e.Apellido, AVG(c.Nota) AS Promedio
FROM Calificacion c
JOIN Inscripcion i ON c.InscripcionID = i.InscripcionID
JOIN Estudiante e ON e.EstudianteID = i.EstudianteID
GROUP BY e.EstudianteID
ORDER BY Promedio DESC
LIMIT 5;
