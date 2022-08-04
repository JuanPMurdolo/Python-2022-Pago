#Títulos, etiquetas y leyendas
#Siguiendo con el gráfico de ahorros veamos como podemos personalizarlo:
import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))

plt.plot(ahorros)
plt.show() 
#Podemos añadir al gráfico el titulo Ahorros del primer semestre y unas etiquetas para los ejes X e Y con Meses y Cantidad en € respectivamente:
plt.plot(ahorros)                         # Añadimos el gráfico
plt.xticks(mapeado, meses)                # Mapeamos los valores horizontales
plt.xlim(1, 4)                            # Configuramos el límite horizontal
plt.title("Ahorros del primer semestre")  # Configuramos el título
plt.xlabel("Meses")                       # Configuramos la etiqueta del eje X
plt.ylabel("Cantidad en $")               # Configuramos la etiqueta del eje Y
plt.show()                                # Finalmente lo mostramos

'''
Otro elemento informativo que podemos añadir son las leyendas plt.legend.

Podemos elegir una localización a partir de las distintas opciones que nos indican en la documentación de matplotlib:

0: best
1: upper right
2: upper left
3: lower left
4: lower right
5: right
6: center left
7: center right
8: lower center
9: upper center
10: center
Por defecto se usa la opción 0 para detectar automáticamente el mejor sitio donde poner la leyenda:
'''
plt.plot(ahorros)                         # Añadimos el gráfico
plt.xticks(mapeado, meses)                # Mapeamos los valores horizontales
plt.xlim(1, 4)                            # Configuramos el límite horizontal
plt.title("Ahorros del primer semestre")  # Configuramos el título
plt.xlabel("Meses")                       # Configuramos la etiqueta del eje X
plt.ylabel("Cantidad en €")               # Configuramos la etiqueta del eje Y
plt.legend(loc=4)                         # Mostramos la leyenda
plt.show()                                # Finalmente lo mostramos

#Van a ver que aparece un cuadradito pero no muestra nada, 
#eso es porque tenemos que configurar el texto del gráfico, algo que definiremos pasando una label a plot o una list a legend:
plt.plot(ahorros, label="Evolución")      # Añadimos el gráfico con una label
plt.xticks(mapeado, meses)                # Mapeamos los valores horizontales
plt.xlim(1, 4)                            # Configuramos el límite horizontal
plt.title("Ahorros del primer semestre")  # Configuramos el título
plt.xlabel("Meses")                       # Configuramos la etiqueta del eje X
plt.ylabel("Cantidad en €")               # Configuramos la etiqueta del eje Y
plt.legend(["Evolución"], loc=0)          # Mostramos la leyenda
plt.show()                                # Finalmente lo mostramos

#En este escenario donde dibujamos un único vector de datos una leyenda no tiene mucho sentido, 
# pero si en lugar de uno tuviéramos tres vectores representando los ahorros de tres personas la cosa cambiaría:

plt.plot(np.random.randint(100, size=[6]))
plt.plot(np.random.randint(100, size=[6]))
plt.plot(np.random.randint(100, size=[6]))
plt.xticks(mapeado, meses)
plt.xlim(1, 4)
plt.title("Ahorros del primer semestre")
plt.xlabel("Meses")
plt.ylabel("Cantidad en €")
plt.legend(["Pedro", "Marta", "Ana"])
plt.show()

#Esto se denomina visualización de múltiples series, representando cada serie una de las líneas del gráfico.

#Personalización con DataFrame
#Por cierto, ¿podemos dibujar el mismo gráfico utilizando un DataFrame? Pues sí y es más fácil:
import pandas as pd

df = pd.DataFrame(
    data=[
        np.random.randint(100, size=[6]), 
        np.random.randint(100, size=[6]), 
        np.random.randint(100, size=[6])],
    index=['Pedro','Marta','Ana'], 
    columns=['Enero','Febrero','Marzo','Abril','Mayo','Junio'])
print(df)

# Veamos como queda...
plt.plot(df)
plt.show()

# Intercambiamos los ejes con el dataframe transpuesto
plt.plot(df.T)
plt.show()

# Resultado final utilizando un DataFrame
plt.plot(df.T)
plt.xlim(1, 4)
plt.title("Ahorros del primer semestre")
plt.xlabel("Meses")
plt.ylabel("Cantidad en €")
plt.legend(['Pedro','Marta','Ana'])
plt.show()

#Gráficos ingeniosos

#Con esto y un poco de comprensión de listas podemos hacer otro ejemplo muy rápidamente para dibujar las tablas de multiplicar del 1 al 10:

# Tablas de multiplicar del 1 al 10
for t in range(1, 11):
    plt.plot(
        range(1, 11),                   # Eje X
        [t * n for n in range(1, 11)],  # Eje Y
        label=f"Tabla del {t}")         # Leyenda para cada serie
    
plt.title('Tablas')
plt.xlabel('Número')
plt.ylabel('Resultado')
plt.legend()
plt.show()
