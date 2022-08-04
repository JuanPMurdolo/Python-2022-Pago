#Límites

'''
En algunas ocasiones necesitaremos manipular los límites inferiores y superiores de los ejes. Podemos hacerlo gracias a los métodos:

plt.xlim(min, max)
plt.ylim(min, max)
Volvamos al ejemplo de los ahorros:
'''
import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(50,100, size=[6])
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))

plt.plot(ahorros)           # Añadimos el gráfico
plt.xticks(mapeado, meses)  # Mapeamos los valores horizontales
plt.show()                  # Finalmente lo mostramos

#En este gráfico estamos manejando un array de datos aleatorios de 50 a 100. Sin embargo el gráfico establecerá los límites en los meses con más y menos ahorros. 
# Podemos establecer que utilice 0 y 100 como escala para el eje Y con los ahorros aunque no tengamos ningún valor en ese rango:
# Límites verticales
plt.plot(ahorros)           # Añadimos el gráfico
plt.xticks(mapeado, meses)  # Mapeamos los valores horizontales
plt.ylim(0, 100)            # Configuramos el límite vertical
plt.show()                  # Finalmente lo mostramos

#Utilizando los límites podemos centrarnos en una parte específica del gráfico.

#Por ejemplo para mostrar únicamente los meses Febrero, Marzo, Abril y Mayo, podemos limitar el eje X a los valores numéricos de los meses 1, 2, 3 y 4 con un range de 1 a 4:

# Límites horizontales
plt.plot(ahorros)           # Añadimos el gráfico
plt.xticks(mapeado, meses)  # Mapeamos los valores horizontales
plt.xlim(1, 4)              # Configuramos el límite horizontal
plt.ylim(0, 100)            # Configuramos el límite vertical
plt.show()                  # Finalmente lo mostramos

#En cierta forma podemos considerarlo una manera de hacer zoom.
