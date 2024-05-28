"""
Paquetes:
Directorios (carpetas) donde se almacenan módulos relacionados entre sí

¿Para qué sirve?
Para organizar mejor el código y poder reutilizar mejor (modularizacióm y reutilizacion)

¿Cómo se crea un paquete?
Crear una carpeta o directorio con un archivo dentro llamado __init__.py

Lo que hace __init__.py es "convertir" un directorio en un modulo (paquete)
que contiene otros modulos, y esto lo hace para poder importarlos

"""
from Paquete.funcionesNumericas import *;
from Paquete.funcionesCadena import *;

print(multiplicar(5, 6));
print(contarLetras("Hello"));
