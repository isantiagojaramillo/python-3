# Raise: Sirve para lanzar de forma intencional excepciones en Python.

def evaluarNota(nota):
    if nota < 0:
        # print("Nota no valida");
        #raise ZeroDivisionError("No se permiten valores negativos");
        raise ValueError("Valor incorrecto");
    elif nota >= 16:
        print("Excelente");
    elif nota >= 11:
        print("Aprobado");
    else:
        print("No aprobado");

evaluarNota(-1);

print("Este es el fin del mi programa");
