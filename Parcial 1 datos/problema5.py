# Define una estructura que almacene los datos de un estudiante (nombre, 
# matrícula, calificación). Luego, escribe una función que reciba un arreglo de 
# estudiantes y devuelva el nombre del estudiante con la calificación más alta. 


class Estudiante:
    def __init__(self, nombre, matricula, calificacion):
        self.nombre = nombre
        self.matricula = matricula
        self.calificacion = calificacion

def estudiante_mejor_calificacion(estudiantes):
    #si no hay estudiantes, devolver None
    if not estudiantes:
        return None

    mejor = estudiantes[0]
    for estudiante in estudiantes[1:]:
        if estudiante.calificacion > mejor.calificacion:
            mejor = estudiante
    return mejor.nombre

#lista:
estudiantes = [
    Estudiante("sofia", "#0001", 9.5),
    Estudiante("Jose", "#0002", 9.2),
    Estudiante("Marco", "#0003", 7.3)
]

nombre_mejor = estudiante_mejor_calificacion(estudiantes)
print("El estudiante con la calificación más alta es:", nombre_mejor)

