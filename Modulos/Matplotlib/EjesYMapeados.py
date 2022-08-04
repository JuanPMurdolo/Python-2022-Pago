#Ejes y mapeados
'''
Como vimos los DataFrames automatizan gran parte del trabajo gracias a las etiquetas,
pero también podemos configurar manualmente la información de los ejes en caso de trabajar con listas o arrays:
'''
import numpy as np
import matplotlib.pyplot as plt
import pylab

# Generamos un array con ahorros de prueba
ahorros = np.random.randint(100, size=6)

# Gráficamos sin etiquetas
plt.plot(ahorros)
pylab.show()

#Mapeado de texto en los ejes
#Para añadir información textual a un eje necesitamos mapear datos en rangos de índices utilizando los métodos xticks e yticks:

# Definimos una lista con los meses para el eje horizontal
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']

#Mapeamos un rango de índices para el eje horizontal
plt.plot(ahorros)
plt.xticks([0,1,2,3,4,5], meses)

#Por cierto, para mostrar en el output de una celda solo el gráfico podemos utilizar específicamente su método show:
plt.plot(ahorros)
plt.xticks(range(len(meses)), meses)
#Debemos tener en cuenta que aunque tengamos texto mapeado, el verdadero valor del eje X es en realidad un rango incremental de números manejado automáticamente.

#Ejes X e Y
#Al utilizar un único vector en el método plot éste lo toma como los valores del eje Y y genera el X automáticamente a partir de su longitud:
y = np.random.randint(20, size=[6])
plt.plot(y)
plt.show()

#Es posible modificar los valores del eje X si los pasamos en otro vector o lista como primer parámetro (siempre que el número de elementos concuerde):
x = ["A", "B", "C", "D", "E", "F"]
plt.plot(x, y)
plt.show()

#Gráficos invertidos
#Algo interesante es que cambiando el orden de los ejes podemos generar un gráfico invertido:
plt.plot(y, x)
plt.show()

#Ejemplo curioso

#¿Qué ocurriría si los valores en X también fueran aleatorios?.
x = np.random.randint(20, size=[6])
y = np.random.randint(20, size=[6])

plt.plot(x, y)
plt.show()
#Como vemos se genera un gráfico muy extraño.
#Un gráfico lineal se rige en función del tiempo, eso implica que uno de los ejes es incremental. 
# Al generar valores aleatorios hemos "roto" esa lógica y el resultado es un gráfico donde las líneas se cruzan por todas partes.






