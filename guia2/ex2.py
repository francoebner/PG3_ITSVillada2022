class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: " + str(self.nombre))
        print("Nota: " + str(self.nota))

    def estado(self):
        if self.nota >= 6:
            print("aprobado")
        else:
            print("desaprobado")


Alumno1 = Alumno("Manolo", 7)
Alumno2 = Alumno("juancho", 3)
Alumno1.imprimir()
Alumno1.estado()
Alumno2.imprimir()
Alumno2.estado()