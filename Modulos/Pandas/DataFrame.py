#La clase DataFrame
'''
Un DataFrame es una agrupación de Series unidas bajo los mismos índices dando como resultado estructuras similares a tablas donde representar todo tipo de información.

Cada serie del DataFrame se puede considerar una columna a la cuál podemos establecer un nombre:

'''
from matplotlib.cbook import print_cycles
import pandas as pd
import numpy as np

array = np.random.uniform(-10, 10, size=[4,4])

df = pd.DataFrame(array, index=['A','B','C','D'], columns=['W','X','Y','Z'])
print(df)
print(type(df))

#Trabajando con DataFrames
#Podemos consultar una columna mediante su nombre:
print(df['X'])
#Como vemos una columna es en realidad una serie:
print(type(df['X']))
#También podemos consultar varias columnas pasando una lista con los nombres:
print(df[['Y','Z']])

#Añadir una columna
df['TOTAL'] = df['W'] + df['X'] + df['Y'] + df['Z']
print(df)

#Borrar una columna
df.drop('TOTAL', axis=1)
# No se modifica el df original
print(df)
# A no ser que le indiquemos explícitamente
df.drop('TOTAL', axis=1, inplace=True)
print(df)

#Borrar una fila
df.drop('D', axis=0)

#Seleccionar filas
df.loc['C']

#También podemos utilizar el índice:
df.iloc[2]

# Seleccionar subset
# Fila C y columna Z 
df.loc['C','Z']
# Filas A,B y columnas W,Y
df.loc[['A','B'],['W','Y']]

#Selección condicionada
#Una de las mayores utilidades de los `DataFrames`
#es su capacidad para realizar consultas condicionadas:
print(df)
#registros >0
print(df>0)
# Valor de los registros >0
df[df>0]
# Valor de los registros cuando X>0
df[df['X']>0]
# Valor de los registros en las columnas Y,Z si X>0
df[df['X']>0][['Y','Z']]

#Se pueden unir condiciones usando los operadores or con | y and con &:
# Valor de los registros cuando X>0 o Z<0
df[(df['X']>0) | (df['Z'] < 0)]
# Valor de los registros en las columnas W e Y cuando X>0 o Z<0
df[(df['X']>0) | (df['Z'] < 0)][['W','Y']]

#Modificar índices
# Creamos de nuevo el dataframe
array = np.random.uniform(-10, 10, size=[4,4])
df = pd.DataFrame(array, index=['A','B','C','D'], columns=['W','X','Y','Z'])
# Añadimos una nueva Serie con el nombre de los índices
df['Códigos'] = ['AA','BB','CC','DD']
print(df)
# Substituimos los índices de las filas
df.set_index('Códigos')
# No se guardan por defecto
print(df)
# A no ser que lo especifiquemos explícitamente
df.set_index('Códigos', inplace=True)
print(df)
# consultamos una fila con el nuevo índice
print(df.loc['AA'])

#Índices por defecto

# Reiniciamos los índices y borramos los anteriores explícitamente
df.reset_index(drop=True, inplace=True)

print(df)
