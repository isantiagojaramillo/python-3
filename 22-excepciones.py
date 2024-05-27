# Excepción: Error en tiempo de ejecución (durante la ejecucion de un programa)

numero1 = 20;
numero2 = 0;

# print("La división de {} entre {} es:".format(numero1, numero2, (numero1 / numero2)));

try:
    resultado = numero1 / numero2;
# except:
except ZeroDivisionError:
    print("No se puede dividir entre 0");

finally: # Siempre se ejecuta
    print("Yo siempre estoy presente");

print("Aquí termina el programa");