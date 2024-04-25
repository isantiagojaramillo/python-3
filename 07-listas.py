lista1 = ["Santi", 25, 98.3, True, "Wolverine", 56.3];
print(lista1);
print(lista1[:]); # Imprimir toda la lista
print(lista1[2]); #Imprimir elemento en la posición 2
print(lista1[-1]); #Imprimir último elemento

print(lista1[0:3]); #Imprime entre el rango de las posiciones del 0 al 3
print(lista1[:2]); #Imprime valores hasta la posición 2
print(lista1[3:]); #Imprime desde la posición 3 en adelante

lista1.append("Nuevo Elemnto"); #añade un elemento al final de la lista
print(lista1);

lista1.insert(4, "Colombia"); # añade un elemento en una posición indicada
print(lista1);

lista1.extend(["Pepe", 110, False]); # extiende la lista
print(lista1);

print(lista1.index("Wolverine")); # indica la posición de un elemento

lista1.remove(56.3); # elimina un elemento
print(lista1);

lista1.pop(); # elimina el último elemento de la lista
print(lista1);

lista2 =["Pepito", "Pepita"];
lista3 = lista1 + lista2; # concatenar listas, (extiende)
print(lista3);

print(lista2 * 4) # repite los valores de una lista

print("Santi" in lista1); # verificar si un elemento esta en la lista(Retorna un valor booleano)


