#Pérdida de datos

#A veces al trabajar con DataFrames nos encontraremos que alguna información puede no cargarse como debería, 
#vamos a ver cómo podemos tratar con esas situaciones.

import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A':[7, 8, -6, 8],
    'B':[12, np.nan, 1, np.nan],
    'C':[4, np.nan, np.nan, np.nan],
    'D':[4, np.nan, -2, -10]})

print(df)

# Comprobar regitros nulos
print(df.isnull())
# Descartar filas con registros nulos
print(df.dropna())
# Descartar columnas con registros nulos
df.dropna(axis=1)
# Mostrar filas con un mínimo dos registros no nulos
df.dropna(thresh=2)
# Mostrar filas con mínimo de tres registros no nulos
df.dropna(thresh=3)
# Rellenar los registros de las filas vacías con un valor
df.fillna(value=0)
# Rellenar los registros de las filas vacías de B con el valor mínimo de B
df['B'].fillna(value=df['B'].min()) #El método min pertenece al conjunto de funciones de agregación para manejar agrupaciones