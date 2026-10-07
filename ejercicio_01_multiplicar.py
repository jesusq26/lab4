"""
EJERCICIO 01: Tabla de multiplicar

1. Pide al usuario ingresar un número
2. Garantice la entrada correcta
3. Imprime la tabla de multiplicar del 1 al 10 del número ingresado. Utilice un bucle for
"""

try:
    numero = float(input("Ingrese un número: "))
    print(f"Tabla de multiplicar del {numero}")
    for i in range(1, 11):
       r = numero * i 
       print(f"{numero} x {i} = {r}")

except ValueError:
    print("Ingrese un número válido.")

