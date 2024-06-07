AlumnosAprobados = 0
alumnosReprobados = 0
AcumuladorPromedio = 0
CantidadAlumno = int(input('Ingrese la cantidad de alumnos: '))

for i in range(1,CantidadAlumno+1,1):
    alumno = input(f'Estudiante {i}, Ingrese su Nombre: ')
    Promedio = float(input('Ingrese su Promedio: '))
    AcumuladorPromedio = AcumuladorPromedio + Promedio

    promedioCurso = AcumuladorPromedio / CantidadAlumno

    if Promedio >= 4:
        print('El Estudiante ha aprobado')
        AlumnosAprobados = AlumnosAprobados+1
    else:
        print('El Estudiante Reprobo')
        alumnosReprobados = alumnosReprobados+1
print(f'El promedio del curso es: {promedioCurso:.1f}')
print(f'La cantidad de aprobados fue de: {AlumnosAprobados}')
print(f'La cantidad de reprobados fue de: {alumnosReprobados}')