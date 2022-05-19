class Operacion:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def operaciones(self):
        print("Suma: " + str(self.numero1 + self.numero2))
        print("Resta: " + str(self.numero1 - self.numero2))
        print("Multiplicacion: " + str(self.numero1 * self.numero2))
        print("Division: " + str(self.numero1 / self.numero2))
print("Numeros: 3 y 2")
o1 = Operacion(6, 2)
o1.operaciones()