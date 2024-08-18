class Persona():

    def __init__(self, apellidoPaterno, apellidoMaterno, nombre):
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.nombre = nombre

    #METODO
    def mostrarNombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

class Estudiante(Persona):
    
    def __init__(self, apellidoPaterno, apellidoMaterno, nombre, profesion):
        super().__init__(apellidoPaterno, apellidoMaterno, nombre)
        self.profesion = profesion


estudiante1 = Estudiante("Torres", "López", "Juan", "Software")
print(estudiante1.mostrarNombreCompleto())
print(estudiante1.profesion)
