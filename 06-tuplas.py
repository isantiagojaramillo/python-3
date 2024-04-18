tupla = (1, 2, 3);
print(tupla);

tupla2 = (7, "Santi", True, 450.1, 16, + 73, "Felicidad", False);
print(tupla2);

tupla3 = (9, 3, (4, 5, 6));
print(tupla3);

print(tupla[1]);

print(tupla2[-1]) #ACCEDER AL ÚLTIMO ELEMENTO

print(tupla2[0:4]); #RANGO DE POSICIONES DEL 0 AL 4

a, b, c = tupla; # Volcar las tuplas
print(a);
print(b);
print(c);

tuplaFinal = tupla + tupla3; #Generar una tupla nueva a partir de otras
print(tuplaFinal);

print(tuplaFinal.count(3)); # Cuantas veces tenemos un 3 

print(tuplaFinal.index(3)); # Primera ocerrencia donde se encuentra un valor


