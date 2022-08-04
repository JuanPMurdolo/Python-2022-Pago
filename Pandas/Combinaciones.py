#Combinaciones

'''
Hay tres técnicas para combinar la información de varios DataFrames:

Concatenación
Fusión
Unión
'''

#Concatenación
#Esta técnica consiste básicamente en juntar las filas de los DataFrames, esto requiere que las dimensiones de los diferentes df concuerden:
import pandas as pd

df1 = pd.DataFrame({'A':['1A','2A'], 'B':['1B','2B'], 'C':['1C','2C']}, index=[1, 2]) 
print(df1)
df2 = pd.DataFrame({'A':['3A','4A','5A'], 'B':['3B','4B','5B'], 'C':['3C','4C','5C']}, index=[3, 4, 5]) 
print(df2)
df3 = pd.DataFrame({'A':['6A','7A'], 'B':['6B','7B'], 'C':['6C','7C']}, index=[6, 7]) 
print(df3)
# Concatenar filas
print(pd.concat([df1, df2, df3]))

#Fusión
#Esta técnica permite fusionar los DataFrames 
# utilizando la misma lógica que se utiliza en SQL para unir tablas, por ejemplo una combinación de dos dataframes a partir de una columna común:

df1 = pd.DataFrame({'clave': ['K1','K2','K3'], 'A': ['1A','2A','3A'], 'B': ['1B','2B','3B']})
print(df1)

df2 = pd.DataFrame({'clave': ['K1','K2','K3'], 'C': ['1C','2C','3C'], 'D': ['1D','2D','3D']})
print(df2)

# Fusionar columnas a partir de una columna común
print(pd.merge(df1, df2, on='clave'))

#Unión
#Esta técnica es muy conveniente para combinar las columnas de dos dataframes indexados:
df1 = pd.DataFrame({'A': ['1A','2A','3A'], 'B': ['1B','2B','3B']}, index=['K1','K2','K3'])
print(df1)

df2 = pd.DataFrame({'C': ['1C','2C','3C'], 'D': ['1D','2D','3D']}, index=['K1','K2','K3'])
print(df2)

# Unir columnas mediante los índices
print(df1.join(df2))

