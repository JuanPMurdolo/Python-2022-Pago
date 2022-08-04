#Operaciones
#Los DataFrames ofrecen varias operaciones básicas

#Rango de fechas
import pandas as pd
import numpy as np

# Rango de fechas para usar de índice en un dataframe
index = pd.date_range("7/15/2022", periods=20)

print(index)

#Consultas rápidas

# Lo utilizamos para rellenar un df con valores aleatorios
df = pd.DataFrame(np.random.randn(20, 4), index=index, columns=["A", "B", "C", "D"])
print(df)

# Primeras filas (cabeza)
print(df.head())
# Primeras tres filas
print(df.head(3))
# Últimas filas (cola)
print(df.tail())
# Últimas tres filas
print(df.tail(3))

#Valores únicos
# Definimos un DataFrame con información de diferentes tipos
df = pd.DataFrame({
      'enteros': [100, 200, 300, 400],
    'decimales': [3.14, 2.72, 1.618, 3.14],
      'cadenas': ['hola','adiós','hola','adiós']})
print(df)
# Array de valores únicos de una columna
df['cadenas'].unique()
# Contador de valores únicos de una columna
df['cadenas'].nunique()
# Dataframe con los de valores únicos y su contador de una columna
df['cadenas'].value_counts()

#Aplicación de funciones
# Método interno de las Series columna
df['decimales'].sum()
# Aplicar una función predefinida
df['cadenas'].apply(len)
# Aplicar una función definida
def doblar(n):
    return n*2
df['enteros'].apply(doblar)

# Aplicar una función anónima
df['enteros'].apply(lambda n: n/3)

# Borrar permanentemente una columna
del df['decimales']
print(df)

#Recuperar índices
# Índices de las columnas
print(df.columns)
# Índice de las filas
print(df.index)

#Aplicar ordenaciones
# Ordenar por columna (inplace=False por defecto)
df.sort_values(by='enteros')
# Ordenar por columna inversamente (inplace=False por defecto)
df.sort_values(by='enteros',ascending=False)
