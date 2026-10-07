"""
EJERCICIO 04: Adivina el número

1. Selecciona un número entero y almacenalo en una variable. 
2. Pide al usuario que lo adivine dentro de un bucle while. 
3. En cada intento, el programa debe indicar si el número buscado es mayor o menor que el ingresado, hasta que lo adivine.
"""

x = 50
y = 0
try:
    while x != y:
        y = int(input("Adivina el numero:"))
        if y < x:
            print("El numero es mayor")
        elif y > x:
            print("El numero es menor")
    print("Adivinaste el numero")

except ValueError:
    print("Ingrese un número válido.")


