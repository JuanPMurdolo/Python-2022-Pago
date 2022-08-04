import numpy as np
import pandas as pd

etiquetas = ['A','B','C','D']
lista = [25,50,75,100]
print(pd.Series(data=lista))
print(pd.Series(data=lista, index=etiquetas))
pd.Series(lista, etiquetas) #es lo mismo que lo anterior

#Con Arrays
array = np.random.randint(50, size=4)
print(array)
# serie básica
print(pd.Series(array))
# serie con etiquetas
print(pd.Series(array, etiquetas))

#Diccionarios
diccionario = {'A':25, 'B':50, 'C':75, 'D':100}
print(pd.Series(diccionario))

#Indices
#Las etiquetas ofrecen una alternativa a los índices 
# numéricos para acceder a la información de forma cómoda:
ingresos = pd.Series([100,300,200], index = ['enero', 'febrero', 'marzo'])

print(ingresos)
# aceso por número
print(ingresos[0])
# acceso por nombre
print(ingresos['enero'])

#Métodos
#Las Series tienen diferentes métodos, como add y 
# subtract para sumar y restar series utilizando los índices:

gastos = pd.Series([100,150,250], index = ['enero', 'febrero', 'marzo'])
print(gastos)
total = ingresos.subtract(gastos)

print(total)
print(ingresos - gastos)

#Tipo de una Serie
print(type(total))