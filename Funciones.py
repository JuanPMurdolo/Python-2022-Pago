"""

1) Realiza una función llamada area_rectangulo() que devuelva el área del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura.

Nota: El área de un rectángulo se obtiene al multiplicar la base por la altura.
"""

def area_rectangulo(base, altura):
    return base*altura

print(area_rectangulo(15,10))

"""
*2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio: *

Nota: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:

import math
print(math.pi)
> 3.1415...
"""
import math

def area_circulo(radio):
    return ((math.pow(radio, 2))*math.pi)
            
print(area_circulo(5))

"""
**3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente**:

* Si el primer número es mayor que el segundo, debe devolver 1.
* Si el primer número es menor que el segundo, debe devolver -1.
* Si ambos números son iguales, debe devolver un 0.

** Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'**
"""
# Completa el ejercicio aquí
def relacion(a, b):
    if (a > b):
        return 1
    elif (a < b):
        return -1
    else:
        return 0

print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))
"""
4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:

Nota: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

** Comprueba el punto intermedio entre -12 y 24**
"""
def intermedio(a,b):
    return (a+b)/2
print(intermedio(-12,24))
"""
5) Realiza una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste
Devolver el límite superior si el número es mayor que éste.
Devolver el número sin cambios si no se supera ningún límite.
** Comprueba el resultado de recortar 15 entre los límites 0 y 10**
"""
def recortar(a,b,c):
    if (a < b):
        return b
    elif (a > c):
        return c
    else:
        return a
print(recortar(15,0,10))
"""
6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:

Por ejemplo:

pares, impares = separar([6,5,2,1,7])
print(pares)   # valdría [2, 6]
print(impares)  # valdría [1, 5, 7]
Nota: Para ordenar una lista automáticamente puedes usar el método .sort().
"""
def separar(lista):
    numeros.sort()
    pares = []
    impares = []
    for i in lista:
        if (i % 2 == 0):
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

numeros = [-12, 84, 13, 20, -33, 101, 9]

pares, impares = separar(numeros)
print(pares)
print(impares)
