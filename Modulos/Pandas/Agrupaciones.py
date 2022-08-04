#Agrupaciones

#La clase DataFrame contiene un método llamado groupby que permite agrupar filas mediante funciones de agregación:
import pandas as pd

# Creamos un diccionario con mucha información
ventas = {
    'Comercial': ['Juan', 'María', 'Manuel', 'Vanesa', 'Ana', 'Marcos'],
    'Empresa': ['Movistar', 'Jazztel', 'Movistar', 'Jazztel', 'Vodafone', 'Vodafone'],
    'Primas': [300, 220, 140, 70, 400, 175]
} 
df = pd.DataFrame(ventas)
print(df)
#Utilizando groupby podemos agrupar las filas en función del nombre de la columna, 
#por ejemplo el nombre de la Empresa, al hacerlo se generará un nuevo objeto de tipo DataFrameGroupBy:
print(df.groupby('Empresa'))
#Este objeto se puede asignar a una variable para trabajar con él a fondo:
por_empresa = df.groupby("Empresa")

#Con los métodos de agregación podemos analizar la información agrupada:

# Lo mismo sin guardar el objeto en una variable
df.groupby('Empresa').mean()

#Otros métodos útiles:
# Desviación estándar (dispersion del conjunto)
print(por_empresa.std())
# Primas mínimas (error)
print(por_empresa.min())
# ID de las primas mínimas
print(por_empresa['Primas'].idxmin())
# Usamos las ID de las primas máximas como fuente del df
print(df.loc[por_empresa['Primas'].idxmin()])
# Primas mínimas
print(df.loc[por_empresa['Primas'].idxmax()])
# Contador de primas por empresa
print(por_empresa.count())
# Reporte de analíticas descriptivas por empresa
print(por_empresa.describe())
# Reporte transpuesto (filas por columnas)
print(por_empresa.describe().transpose())
# Reporte transpuesto de una sola empresa
print(por_empresa.describe().transpose()['Movistar'])