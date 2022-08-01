#Metodo normal
'''
lista = []
for letra in 'casa':
    lista.append(letra)
print(lista)
'''
'''
#Metodo con compresion de listas
lista = [letra for letra in 'casa']
print(lista)
'''
lista = []
#Metodo tradicional
for numero in range(0,11):
    lista.append(numero)
print(lista)

#Metodo con compresion de listas
lista = [numero**2 for numero in range(0,11)]
print(lista)

#Metodo tradicional
lista = []
for numero in range(0,11):
    if numero % 2 == 0:
        lista.append(numero)
print(lista)

#Metodo comprension de lista
lista = [numero for numero in range(0,11) if numero % 2 == 0]
print(lista)

#Metodo tradicional
lista = []
for numero in range(0,11):
    lista.append(numero**2)

pares = []
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

pares = [numero for numero in [numero**2 for numero in range(0,11)] if numero % 2 == 0]
print(pares)

'''
Comprensión de listas
Utiliza todo lo que sabes para generar una lista en una única línea llamada multiples que contenga todos los números múltiples comunes de 2, 3, 4 y 8 entre 0 y 500 (ambos incluidos). No puede contener números repetidos y estos deben estar ordenados de menor a mayor.
'''
multiples = [numero for numero in range(0,500) if numero % 2 == 0 and numero % 3 == 0 and numero % 4 == 0 and numero % 8 == 0]

