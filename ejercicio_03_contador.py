"""
EJERCICIO 03: Contador de vocales

Dada una frase escrita por el usuario, recorre cada letra e indica la cantidad de vocales (a, e, i, o, u) que tiene la palabra.
"""
vocales = 0
v = input("Ingrese una frase: ")
for i in v:
    if i in "aeiouAEIOU":
        vocales += 1
print("Cantidad de vocales:", vocales)