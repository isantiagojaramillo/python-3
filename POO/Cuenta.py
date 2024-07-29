class Cuenta():
    
    def __init__(self, propietario, saldo, moneda):
        self.__propietario = propietario
        self.__saldo = saldo
        self.__moneda = moneda

# Los métodos accesores sirven para leer o modificar 
# propiedades dentro de una clase, propiedades que se 
# encuentran encapsuladas y que no se pueden modificar 
# ni leer desde fuera de la clase

    # Getters (Métodos GET)
    def get_Salso(self):
        return self.__saldo
    
    def get_Propietario(self):
        return self.__propietario
    
    def get_Moneda(self):
        return self.__moneda

    # Setters (Métodos Set)
    def set_Moneda(self, moneda):
        self.__moneda = moneda

cuenta1 = Cuenta("Santiago J", 1500, "Soles")
print(cuenta1.get_Salso())
print(cuenta1.get_Moneda())
cuenta1.set_Moneda("Dolares")
print(cuenta1.get_Moneda())
