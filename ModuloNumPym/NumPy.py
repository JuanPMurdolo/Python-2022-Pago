'''
Configuración previa
El análisis de datos básico en Python se realiza utilizando tres bibliotecas que se complementan perfectamente entre ellas:

NumPy: Para manejar arrays.
Pandas: Para manejar dataframes.
Matplotlib: Para visualizar gráficos.
Son externas a Python por lo que tenemos que instalarlas para poder utilizarlas:

pip install numpy pandas matplotlib
También se puede instalar desde el propio Jupyter Notebook con una exclamación delante:

!pip install numpy pandas matplotlib
Tardará un rato en ejecutar la celda pero veremos el resultado:

!pip install numpy pandas matplotlib
'''

# Normalmente se suele importar numpy como np
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Podemos crear un arreglo a partir de
array = np.array([1, 2, 3, 4, 5])

# Y lo mostramos
print(array)
print(type(array))
print(array.ndim)

#En la tupla (5,) el primer valor indica a que el array
#tiene 5 elementos en la primera dimensión (de ancho).
print(array.shape)
#Ahora bien, si definimos un array a partir de una lista anidada formada por dos sublistas:
array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
print(array)
print(array.ndim)
print(array.ndim)

'''
En este caso array se muestra como una tabla de 2 filas y 5 columnas, números que precisamente concuerdan con la forma (2, 5).

Estas estructuras formadas por filas y columnas parecidas a una tabla tienen dos dimensiones, ancho y alto.

También se conocen como vectores multidimensionales o matrices 2D.
'''
#Tipo de datos
#Podemos consultar el tipo de un array, 
# por ejemplo éste que contiene sólo enteros:
array = np.array([1, 2, 3, 4, 5])
print(array.dtype)
array = np.array([1, 2, 3, 4, 5, 6.1234])
print(array.dtype)
array = np.array(["Hola", "que", "tal"])
print(array.dtype)
array = np.array(["Hola", 1234, 3.1415])
print(array.dtype)
print(array)
tabla = pd.DataFrame(
    np.random.randint(0, 100, size=(4, 3)),
    columns=['Pepe', 'María', 'Juan'])

print(tabla)
tabla.plot()
plt.show()