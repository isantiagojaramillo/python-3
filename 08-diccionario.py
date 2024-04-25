miDiccionario = {"España": "Madrid", "Peru": "Lima", "Alemania": "Berlin"};

print(miDiccionario["Peru"]); # imprime el valor de la clave perú
print(miDiccionario);

miDiccionario["Colombia"] = "Medellín"; # agregar un elemento al diccionario
print(miDiccionario);

miDiccionario["España"] = "Barcelona"; # cambia el valor de la clave, si ya se encuentra en el diccionario
print(miDiccionario);

# función o clausula del
del miDiccionario["España"]; # elimina tanto la clave como el valor

dic2 = {"Garcia": "Oscar", 25:True, "Sueldo": 150.00};
print(dic2[25]); # las claves pueden almacenar cualquier valor

# podemos usar una tupla, para definir las llaves que va a tener el diccionario
llaves = ("España", "Francia", "Inglaterra");
dicPaises = {llaves[0]: "Madrid", llaves[1]: "Paris", llaves[2]: "Londres"};
print(dicPaises);

# podemos tener un diccionario dentro de otro
datosPersonales = {"Apellido": "Garcia", "Anios": {1:2010, 2:2011, 3:2012, 4:2013, 5:2014}};
print(datosPersonales);
print(datosPersonales["Anios"]);

print(datosPersonales.get('Apellido', "Santi")); # si no encuentra el valor de la clave, devolvera el otro valor especificado

print(datosPersonales.keys()); # saber las llaves de nuestro diccionario
llaves = tuple(datosPersonales.keys());
print(llaves);

print(datosPersonales.values()); # saber los valores de nuestro diccionario
valores = list(datosPersonales.values());
print(llaves);
