class Persona:
    def __init__(self):
        self.nombre = input("nombre: ")
        self.edad = int(input("edad: "))

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("sueldo: "))

    def mostrar(self):
        super().mostrar()
        print("Sueldo: ", self.sueldo)
        if self.sueldo > 3000:
            print("debe pagar impuestos")

Persona1 = Persona()
Persona1.mostrar()

Empleado1 = Empleado()
Empleado1.mostrar()