'''
Configuración previa
Instalación de Matplotlib por si alguien no lo tiene:

pip install matplotlib
También se puede instalar desde el propio Jupyter Notebook con una exclamación delante:

!pip install matplotlib
'''

#Primeros gráficos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab


#Usando listas
#Supongamos que necesitamos un gráfico que muestre los ahorros que hemos tenido durante los últimos 4 meses.
#Vamos a declarar una lista con ellos:

ahorros = [52, 104, 32, 65, 15, 76]
plt.plot(ahorros)
pylab.show()

#Este gráfico tiene dos ejes, el horizontal (X) con 4 números de 0 a 3 y el vertical con los ahorros (Y) 
# que empieza con el mínimo 30 hasta el máximo 100. Estos números corresponden 
# a los índices de los valores en la lista y matplotlib genera una escala a partir de ellos.

#Usando arrays
#También podemos crear gráficos a partir de arrays, como este array aleatorio de ahorros para el último año (12 meses):
ahorros = np.random.randint(100, size=[6])
plt.plot(ahorros)
pylab.show()

#Usando DataFrames
#Finalmente, también podemos crear un gráfico a partir de un dataframe como el anterior pero con etiquetas
df = pd.DataFrame(ahorros, index=['Enero','Febrero','Marzo','Abril','Mayo','Junio'])
plt.plot(df)
pylab.show()

#Los DataFrames nos permiten configurar fácilmente el texto para los ejes del gráfico.

#También tienen su propio método plot, con lo cuál no tenemos que pasarlos a plt.plot, 
# pero no vamos a profundizar en él porque tiene sus propias configuraciones y sería como aprender dos veces lo mismo:
df.plot()
pylab.show()






