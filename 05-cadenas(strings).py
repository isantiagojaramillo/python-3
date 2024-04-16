texto = "Bienvenido al nuevo mundo de George2024";

print(texto);
print(texto.lower());
print(texto.upper());
print(texto.title());

print(texto.find("al"));
print(texto.count("e"));

textoFinal = texto.replace("a", "3");
print(textoFinal);

valor = texto.isnumeric();
print(valor);

cadenaSeparada = texto.split(" ");
print(cadenaSeparada);
