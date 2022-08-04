#Operaciones Basicas
#Suma
#Por ejemplo las operaciones suma y resta 
#requieren que los arrays tengan la misma forma,
#es decir, mismo número y tamaño de las dimensiones.
import numpy as np

# Dos arrays
arr_1 = np.array([1,2,3,4])
arr_2 = np.array([5,6,7,8])

# Los sumamos
arr_1 + arr_2

#Si no tienen la misma forma no se pueden sumar:
arr_3 = np.array([9,10])
arr_2 + arr_3
#Resta
arr_2 - arr_1

#Producto
#En el caso del producto, la divisón y la potencia se pueden 
# operar arrays de las mismas dimensiones si el número de 
# columnas de la primera coincide con el número de filas 
# de la segunda:
# Dos arrays
arr_1 = np.array([1,2,3,4])
arr_2 = np.array([2,3,4,5])

# Los multiplicamos
arr_1 * arr_2
#Se puede multiplicar un array por un numero
arr_1 * 10
#En este caso sería equivalente a multiplicar un array con una fila y una columna 1x1:
arr_1 * np.array(10)
#Division
#Igual que el producto, 
# la división entre arrays se basa en dividir cada
#  elemento de un array por el elemento en la misma 
# posición del otro:

arr_1 / arr_2
#También podemos dividir todos sus elementos por un número:
arr_1 / 2
#Algo interesante que podemos hacer con la división es conseguir el arreglo inverso o recíproco dividiendo 1 entre el array:
1 / arr_1
#Esto es equivalente hacer la potencia a -1 del array:
arr_1 ** -1
#No podemos elevar a un entero negativo, pero sí podemos indicar la elevación a-1. e indicar un decimal:
arr_1 ** -1.

#Potencia
arr_1 ** arr_2
#Operaciones en arrays 2D
arr_5 = np.array([[1,2],[3,4]])
arr_6 = np.array([[5,6],[7,8]])

arr_5 + arr_6

#Se realiza la operación entre los valores que comparten posición en los arrays:

#[[1+5, 2+6], [3+7, 4+8]] = [[6, 8], [10, 12]]

#De igual forma funcionaría el producto, división y potencia por un número:

arr_5 * 3
#[[1x3, 2x3], [3x3, 4x3]] = [[3, 6], [9, 12]]

#Podemos multiplicar, dividir y potenciar matrices siempre que el número de 
# columnas de la primera coincida con el número de reglones de la segunda:

arr_5 * np.array([5,10])
#Si esto no se cumple...
#arr_5 * np.array([5,10,15]) #explota