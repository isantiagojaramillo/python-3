"""
¿En qué consiste la programación orientada a objetos?

En trasladar la naturaleza de los objetos de la vida real a
código de programación (en algún lenguaje de programación como python)

Los objetos de la realidad tienen características (atributos o propiedades)
y funcionalidades o comportamientos (funciones o métodos)

Ventajas:
- Modularización (división en pequeñas partes) de un programa completo.
- Código fuente muy reutilizable.
- Código fuete más fácil de incrementar en el futuro y mantener.
- Si existe un fallo en una pequeña parte del código el programa
completo no debe fallar necesariamente. Además, es más fácil de corregir esos
fallos.
- Encapsulamiento: Ocultamiento del funcionamiento interno de un objeto.

"""

class Persona():
    # Propiedades, características o atributos:
    apellidos = ""
    nombres = ""
    edad = 0
    despierta = False

    # Funcionalidades:
    def despertar(self):
        # self: Parametro que hace referencia a la instancia perteneciente a la clase
        self.despierta = True
        print("Buen día")

persona1 = Persona()
persona1.apellidos = "Garcia Fuentes"
print(persona1.apellidos)
persona1.despertar()
print(persona1.despierta)

persona2 = Persona()
persona2.apellidos = "PAZ TORRES"
print(persona2.apellidos)
#persona2.despertar()
print(persona2.despierta)
