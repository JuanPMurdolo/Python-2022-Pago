#Estilos de línea y marcadores

import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))

arr_pedro = np.random.randint(100, size=[6])
arr_marta = np.random.randint(100, size=[6])
arr_ana = np.random.randint(100, size=[6])

'''
Líneas
Tenemos las siguientes propiedades básicas:

linewidth (lw): Ancho de la línea
linestyle (ls): Estilo de la línea
color: Color de la línea (número y decimal)
alpha: Opacidad de la línea (de 0 a 1)
'''

# Configuración de las líneas
plt.plot(arr_pedro, label="Pedro", color="red", ls="-", lw="5")
plt.plot(arr_marta, label="Marta", color="#0000ff", ls="--", lw="4")
plt.plot(arr_ana, label="Ana", color="green", ls="-.", lw="3")
plt.xticks(mapeado, meses)
plt.legend()
plt.show()

'''
Marcadores
Hacen referencia a los puntos o vértices donde se dibujan los valores:

marker: Tipo de marcador
markersize: Tamaño del marcador
markerfacecolor: Color del marcador (número y decimal)
markeredgecolor: Color del borde (número y decimal)
markeredgewidth: Tamaño del borde
'''

# Configuración de los marcadores
plt.plot(arr_pedro, label="Pedro", color="red", ls="-", lw="2", 
         marker="o", markersize="10", markeredgewidth="2", markerfacecolor="yellow", markeredgecolor="red")

plt.plot(arr_marta, label="Marta", color="#0000ff", ls="--", lw="2",
         marker="*", markersize="15", markeredgewidth="2", markerfacecolor="cyan", markeredgecolor="#0000ff")

plt.plot(arr_ana, label="Ana", color="green", ls="-.", lw="2",
         marker="D", markersize="10", markeredgewidth="2", markerfacecolor="lime", markeredgecolor="green")

plt.xticks(mapeado, meses)
plt.legend()
plt.show()

