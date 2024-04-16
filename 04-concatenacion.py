texto1 = "Hola";
texto2 = "Mundo";

# Forma 1
textoFinal = texto1 + " " + texto2;
print(textoFinal);

# Forma 2
print("El saludo es %s %s" % (texto1, texto2));

# Forma 3
saludoFinal = "Saludo: {0} {1}".format(texto1, texto2);
print(saludoFinal);

# Forma 4
saludoFinal2 = "Saludo: {x} {y}".format(x=texto1, y=texto2);
print(saludoFinal2);
