"""
EJERCICIO 06: Compresión de una imagen

Se tiene una imagen de pixeles en blanco y negro de dimensión 1xn. Para efectos prácticos de este ejercicio, esta imagen está
representada por una lista de tamaño n, donde cada posición representa el valor del pixel correspondiente. 

Primero, se quiere verificar que los valores dentro de la imagen sean correctos. Para imágenes en blanco y negro, cada pixel 
ocupa un byte de información. Esto significa que cada valor puede tomar valores entre 0 y 255 (ambos incluídos). Recorra la 
imagen proporcionada y verifique que los valores en cada pixel estan en el rango esperado:
    - Si el valor < 0, reemplace por 0
    - Si el valor > 255, reemplace por 255
    - Si el valor está dentro del rango, mantiene su valor
    - Lleva un conteo de cuantos pixeles modificas

Una vez verificada la imagen, se desea comprimir en función a un número ingresado por el usuario. Aunque existen distintos métodos
de compresión, en este programa se quiere usar la compresión por promedio en bloques deslizantes. Esta consiste en escoger un 
número k entero, donde 1 <= k <= n, que representa el tamaño del bloque seleccionado para promediar, es decir, la cantidad de pixeles
de la imagen original que se van a agrupar para formar un pixel en la imagen comprimirda. Considere que se avanza una posición por
cada promedio a realizar (step). Los valores de los extremos solo se utilizan una vez.

Ej: 
    imagen = [50, 62, 75, 2, 5]
    Con k = 1:
    imagen_comprimida = [50, 62, 75, 2, 5]
    Con k = 2:
    imagen_comprimida = [promedio(50, 62), promedio(62, 75), promedio(75, 2), promedio(2, 5)]
    imagen_comprimida = [52              , 68.5            , 38.5           , 3.5           ]
    Con k = 3:
    imagen_comprimida = [promedio(50, 62, 75), promedio(62, 75, 2), promedio(75, 2, 5)]
    imagen_comprimida = [62.33               , 46.33              , 27.33             ]
    Con k = 4:
    imagen_comprimida = [promedio(50, 62, 75, 2), promedio(62, 75, 2, 5)]
    imagen_comprimida = [47.25                  , 35.25                 ]
    Con k = 5:
    imagen_comprimida = [promedio(50, 62, 75, 2, 5)]
    imagen_comprimida = [38.80                     ]

Nota: Vea que hay una relación entre n, k y n_comp, donde n_comp es el tamaño de la lista comprimida ( k = n - n_comp + 1 )

Pídale al usuario que ingrese el tamaño deseado de la imagen comprimida (n_comp). 
    - Use try/except para evitar que se pare la ejecución si el usuario ingresa algún caracter no numérico
    - Utilice while para asegurar que el numero ingresado no sea mayor al tamaño original y no sea negativo
    - Si el usuario ingresa 0, la imagen comprimida es una lista vacía
    - Si la entrada está bien, haga la compresión de la lista. Esta debe ser de numeros enteros.

Finalmente, muestra el resultado en pantalla: la imagen comprimida y el contador de los pixeles modificados en la imagen original

"""

#########################################################################################################################
## PARTE 1: Definición de imagen

imagen = [100, 98, -3, 0, 56, 86, 7, 300, 255, 256, 35, -621, -1, 50, 126, 201]

#########################################################################################################################
## PARTE 2: Verificación de la imagen 

# Recorra la lista y verifique que los valores de los pixeles estan en el rango esperado [0, 255]. Lleve conteo de los valores
# modificados 

contador_modificados = 0

for i in range(len(imagen)):
    if imagen[i] < 0:
        imagen[i] = 0
        contador_modificados += 1
    elif imagen[i] > 255:
        imagen[i] = 255
        contador_modificados += 1

#########################################################################################################################
## PARTE 3: Pedir nuevo tamaño deseado 

n = len(imagen)
n_comp = -1  

while n_comp < 0 or n_comp > n:
    try:
        n_comp = int(input("Ingrese un numero para comprimir la imagen: "))
        if n_comp < 0 or n_comp > n:
            print("Ingrese un número del 0 al", n, "para comprimir la imagen")
    except ValueError:
        print("Ingrese un número entero del 0 al", n, "para comprimir la imagen")
        n_comp = -1

#########################################################################################################################
## PARTE 4: Compresión de la imagen  

# Calcule los valores de la imagen comprimida en función a la imagen original y el tamaño deseado (ingresado por el usuario)

imagen_comprimida = []
if n_comp > 0:
    k = n - n_comp + 1            
    for i in range(n_comp):         
        b = imagen[i:i + k]
        imagen_comprimida.append(sum(b) // k)

#########################################################################################################################
## PARTE 5: Mostrar resultados  

# Imprima en pantalla el resultado de la compresión, junto con la cantidad de pixeles no validos de la imagen original

print("La imagen comprimida es:", imagen_comprimida)
print("Cantidad de pixeles modificados en la imagen original:", contador_modificados)