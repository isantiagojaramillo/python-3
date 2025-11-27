menu = "Menu\n"
menu += "Matematicas\n";
menu += "Biología\n";
menu += "Lenguaje\n";
menu += "Ciencias\n";

curso = input(menu +"Ingrese el curso deseado: \n").capitalize();

if curso in ("Matematicas", "Biología", "Lenguaje", "Ciencias"):
    print("Curso {} seleccionado".format(curso));
else:
    print("No existe ese curso");
