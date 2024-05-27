# Break: Permite salir de un bucle cuando se cumple una condicion

# for numero in range(1,6):
#     if numero == 3:
#         break;
#     print("El numero es: {}".format(numero));

# print("bucle terminado");

#Continue: Omite una parte del bucle cuando se cumple una condición y continue con el resto

# for numero in range(1,6):
#     if numero == 3:
#         continue;
#     print("El numero es: {}".format(numero));

# print("bucle terminado");

# Pass: Permite continuar con una sentencia o funcion que ya no tiene algún bloque de código útil.

for numero in range(1,6):
    if numero <= 3:
        pass;
    else:
        print("El siguiente valor es mayor a 3");
    print("El numero es: {}".format(numero));

print("bucle terminado");
