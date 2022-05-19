class persona:
    def nombre(self, nom):
        self.nombre = nom
    def imprimir(self):
        print("El nombre es: ", self.nombre)
persona1 = persona()
persona1.nombre("teodoro reyna :)")
persona1.imprimir()
persona2 = persona()
persona2.nombre(input("ingrese su nombre"))
persona2.imprimir()