"""
EJERCICIO 02: Sumatoria

1. Pide números enteros al usuario constantemente usando un bucle while. 
2. Suma los valores ingresados.
3. Detén el bucle únicamente cuando el usuario ingrese el número 0. 
4. Al final, muestra la suma total.
"""
x = 1
y = 0

try:
    while x != 0:
      x = float(input("Ingrese un numero:"))
      r = x
      y = y + r
    print("Suma total:", y)

except ValueError:
    print("Ingrese un número válido.")