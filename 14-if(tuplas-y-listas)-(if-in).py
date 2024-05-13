menu = "Menu\n";
menu += "Matematicas\n";
menu += "Biología\n";
menu += "Lenguaje\n";
menu += "Ciencias\n";

curso = input("Ingrese el curso deseado: \n"+ menu).capitalize();

if curso in ("Matematicas", "Biologia", "Lenguaje", "Ciencias"):
    print("Curso {} seleccionado".format(curso));
else:
    print("No existe ese curso");
