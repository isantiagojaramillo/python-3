# Cuando indicamos un * adelate del párametro de una función
# estamos indicando que se va a recibir un número indeterminado
# de parámetros. Además, esos parámetros se recibiran en forma de tupla

# def devuelveLenguajes(*lenguaje):
#     for leng in lenguaje:
#         yield leng;

# lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "Javascript");

# print(next(lenguajesObtenidos));
# print(next(lenguajesObtenidos));


# def devuelveLenguajes(*lenguaje):
#     for leng in lenguaje:
#         for letra in leng:
#             yield letra;

# lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "Javascript");

# print(next(lenguajesObtenidos));
# print(next(lenguajesObtenidos));

def devuelveLenguajes(*lenguaje):
    for leng in lenguaje:
        yield from leng; # Nos permite crear un objeto iterable dentro de otro objeto iterable

lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "Javascript");

print(next(lenguajesObtenidos));
print(next(lenguajesObtenidos));
