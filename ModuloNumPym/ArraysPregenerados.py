'''
Arrays pregenerados
Crear arrays a partir de listas puede ser muy tedioso, por eso numpy integra varias funciones muy útiles para generar arrays de uso común en el álgebra de matrices.

Array de ceros
Un array de ceros es cuando todos sus elementos son ceros. Podemos generarlos con el método zeros:
'''
import numpy as np
#Arrays de ceros
np.zeros(3)
np.zeros([3,3])
#arrays de unos
np.ones([3,3])
#Arrays de identidad
#Los arrays de identidad son matrices cuadradas 
# (con el mismo número de filas que de columnas) 
# donde todos los valores son ceros a excepción 
# de la diagonal donde son unos. 
# Podemos generarlos con el método eye:
np.eye(3)
#De forma similar a como multiplicar un número por 1 da como resulta el mismo número, 
# multiplicar una matriz por su matriz de identidad da como resultado la matriz original. 
# Eso tiene muchas aplicaciones en el álgrebra de matrices, especialmente en el renderizado de gráficos.

#Array de rangos
#Por último pero no por ello menos importante también
#  es posible generar arrays a partir de un rango de valores. 
# Para hacerlo utilizaríamos el método arange:
# Rango de 0 a 4
np.arange(4)
# Rango 0 a 4 decimal
np.arange(4.)
# Rango de -3 a 4
np.arange(-3, 3)
# Rango de 20 números a partir de 0 cada 5 números
np.arange(0, 20, 5)

