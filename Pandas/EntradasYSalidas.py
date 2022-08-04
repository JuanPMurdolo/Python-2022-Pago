#Entradas y Salidas

import numpy as np
import pandas as pd

# Definimos un dataframe con datos de ejemplos
df = pd.DataFrame(np.random.randn(10, 5), columns=["A", "B", "C", "D", "E"])
print(df)

#CSV

#Guardar en CSV
df.to_csv('datos.csv', index=False)
# Borramos el df de la memoria
del(df)

#Cargar desde CSV
df = pd.read_csv('datos.csv')
print(df)

#JSON

#Guardar
df.to_json('datos.json')
# Borramos el df de la memoria
del(df)

#Cargar
df = pd.read_json('datos.json')
print(df)

# Excel
#Necesitamos instalar el módulo `openpyxl` para generar y leer este formato: pip install openpyxl

#Una vez instalado ese modulo, para guardar
df.to_excel('datos.xlsx', sheet_name='Sheet1', index=False)
# Borramos el df de la memoria
del(df)

#Para cargar
df = pd.read_excel('datos.xlsx', sheet_name='Sheet1')
print(df)

#HTML
#Podemos extraer información directamente desde tablas de páginas web a partir de la URL.
#Esto se consigue haciendo web scrapping con los módulos lxml y BeautifulSoup4, por lo que necesitamos instalarlos:
#pip install lxml BeautifulSoup4
#Una vez instalado lxml y BeautifulSoup4 reiniciamos el kernel (botón girando al lado de stop) y ya estaremos listos:
# Realizamos un scrapping de una tabla de la wikipedia
df = pd.read_html('https://web.archive.org/web/20220717170349/https://en.wikipedia.org/wiki/List_of_countries_by_past_fertility_rate')
#Si se encuentra más de una tabla (como en el caso del ejemplo), podemos hacer referencia al primero a través del índice:
print(df[2])
#Podemos hacer un poco de limpieza y dejar los datos presentables:

# Guardamos el dataframe
fertility_rate = df[2]
fertility_rate.head()

# Renombramos la primera columna para que sea más fácil consultarla
fertility_rate.rename(columns = {'Country/dependent territory':'Country'}, inplace=True)
fertility_rate
#Ahora podemos realizar consultas cómodamente:

# Índice de natalidad por país entre los años 2010-2015
fertility_rate[["Country", "2010–2015"]]

# Misma consulta aplicando el styler para esconder la primera columna
fertility_rate[["Country", "2010–2015"]].head().style.hide(axis=0)

# Índice de natalidad por país entre los años 1985–1990 ordenado de más a menos (primeros resultados)
fertility_rate[["Country", "1985–1990"]].sort_values(by="1985–1990", ascending=False).head().style.hide(axis=0)

# Índice de natalidad por país entre los años 1985–1990 ordenado de más o menos (últimos resultados)
fertility_rate[["Country", "1985–1990"]].sort_values(by="1985–1990", ascending=False).tail().style.hide(axis=0)

# Vamos a transformar todas las columnas desde la segunda hasta la última a valores númericos
fertility_rate = fertility_rate[1:][:].apply(pd.to_numeric, errors='coerce')

# Ahora podemos consultar la media del índice de natalidad para cada año
fertility_rate.mean()[1:]

#Con Matplotlib se pueden graficar estos resultados fácilmente:
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = 10,5
fertility_rate.mean()[1:].plot(kind='line', xlabel="Períodos", ylabel="Media de natalidad mundial")



