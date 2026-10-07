"""
EJERCICIO 05: Menú de cómputo geométrico.

Complete las funciones para que al ejecutar el programa, se muestre el menú y se le pida al usuario ingresar una de las opciones
(1 - 4). 
    - Si escoge 1, se pide ingresar el valor del radio, se calcula el radio y se muestra en pantalla
    - Si se escoge 2, se pide ingresar el valor de la base y la altura, se calcula el area del rectángulo y se muestra en pantalla
    - Si se escoge 3, se pide ingresar el valor de la base y la altura, se calcula el perímetro del rectángulo y se muestra en pantalla
    - Si se escoge 4, se sale del menú y termina el programa
    - Si se ingresa cualquier otra opcion, se imprime "Opción inválida. Intente de nuevo."

"""

def area_circulo(radio):
    r = (3.1416 * radio ** 2)
    print("El área del círculo es:", r)

def area_triangulo(x, y): 
    a = (x * y)/2
    print("El área del triángulo es:", a)
   
def perimetro_rectangulo(x, y):
    p = 2 * (x + y)
    print("El perímetro del rectángulo es:", p)

def menu():
    activo = True
    while activo:
        print("CALCULADORA GEOMÉTRICA")
        print("1. Área de un Círculo")
        print("2. Área de un Triángulo")
        print("3. Perímetro de un Rectángulo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        match opcion:
            case "1":
                x = int(input("Ingrese el radio del círculo: "))
                area_circulo(x)
            case "2":
                x = int(input("Ingrese la base del rectángulo: "))
                y = int(input("Ingrese la altura del rectángulo: "))
                area_triangulo(x, y)
            case "3":
                x = int(input("Ingrese la base del rectángulo: "))
                y = int(input("Ingrese la altura del rectángulo: "))
                perimetro_rectangulo(x, y)
            case "4":
                print("Saliendo...")
                activo = False
            case _:
                print("Opción inválida. Intente de nuevo.")

menu()