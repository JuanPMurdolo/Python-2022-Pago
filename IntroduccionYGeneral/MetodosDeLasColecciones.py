'''1) Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:

un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro
En este otro:

Un día que el viento soplaba con fuerza...
- Mira como se mueve aquella banderola -dijo un monje.
- Lo que se mueve es el viento -respondió otro monje.
- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
Lo único prohibido es modificar directamente el texto'''

texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

lista = texto.split('#')
print(lista[0]+'...')
print('-',lista[1])
print('-',lista[2])
print('-',lista[3])

'''
2) Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

Borrar los elementos duplicados
Ordenar la lista de mayor a menor
Eliminar todos los números impares
Realizar una suma de todos los números que quedan
Añadir como primer elemento de la lista la suma realizada
Devolver la lista modificada
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el pr.imer número de la lista, tal que así:
nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )
> True
Nota: La función sum(lista) devuelve una suma de los elementos de una lista
'''

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modificar(lista) -> list:
    for i in lista:
        if lista.count(i) > 1:
            lista.remove(i)        
    lista.sort()
    for i in lista:
        if i % 2 != 0:
            lista.remove(i)
    lista.insert(0, sum(lista))
    return lista

listaDos = modificar(lista)
print(listaDos[0] == sum(listaDos[1:]))


