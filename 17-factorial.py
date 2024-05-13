# Factorial: Es el proceso de todos los numeros positivos enteros comprendidos entre uno y un determinado numero

# Factorial de 5:  1*2*3*4*5 = 120
# Factorial de 4: 1*2*3*4 = 24

numero = int(input("Ingrese un número: "));

factorial = 1;

for n in range(1, (numero +1)):
    factorial = factorial * n;

print("El factorial de {} es: {} ".format(numero, factorial));
