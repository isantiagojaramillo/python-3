#Generadores: Permiten extraer valores de una función y almacenarlo
# de uno en uno en objetos iterables que se pueden recorrer
# sin la necesidad de almacenar todos a la vez en la memoria
# RAM.

# def generarMultipos7(limite):
#     numero = 1;
#     listaNumeros = [];

#     while numero <= limite:
#         listaNumeros.append(numero * 7);
#         numero = numero + 1;
#     return listaNumeros;

# print(generarMultipos7(10));

def generarMultipos7(limite):
    numero = 1;

    while numero <= limite:
        yield numero * 7;   #Ceder. La instrucción "Yield" genera un objeto iterable
        numero = numero + 1;

obteniendoMiltiplos7 = generarMultipos7(10);

# print(obteniendoMiltiplos7);

# for n in obteniendoMiltiplos7:
#     print(n);

print(next(obteniendoMiltiplos7));
print("100 lineas de código");
print(next(obteniendoMiltiplos7));
print("100 lineas de código");
print(next(obteniendoMiltiplos7));
