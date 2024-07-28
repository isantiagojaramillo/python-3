class Curso():
    # nombre = "Matemáticas"
    # creditos = 5
    # profesion = "Ingenieria Civil"

    # Función constructora de python. Init nos permite definir el constructor, significa la plantilla base con la cual se va a instanciar un objeto a partir de una clase.
    def __init__(self, nombre, credito, profesion):
        self.nombre = nombre
        self.creditos = credito
        self.profesion = profesion
        self.__imparticion = "Presencial" # Propiedad encapsulada

    def mostrarDatos(self):
        data = "Nombre: {0} / Créditos: {1} / Modo de impartición: {2}"
        print(data.format(self.nombre, self.creditos, self.profesion, self.__imparticion))
        docenteAsignado = self.__verificarDocente()
        if docenteAsignado:
            print("Existe docente asignado")
        else:
            print("No es necesario asignar docente")

    # Función encapsulada
    def __verificarDocente(self):
        print("Verificando si existe docente asignado...")
        if self.__imparticion == "Presencial":
            return True
        else:
            return False


curso1 = Curso("Matemáticas", 5, "Ingenieria Civil")
print(curso1.nombre)
curso1.mostrarDatos()

# curso2 = Curso("Idiomas", 4, "Ingenieria Industrial")
# print(curso2.nombre)
