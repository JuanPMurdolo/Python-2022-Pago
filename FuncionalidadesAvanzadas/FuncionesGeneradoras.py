#yield
'''
Cuando el intérprete Python encuentra una función que incluye un yield (o varios), entiende que al llamar esta función no obtendremos un valor devuelto con un return, sino que obtendremos un generador (generator).

Un generador se comporta parecido a una lista, en el sentido que puede ser recorrida con un iterador 
- la diferencia es que los valores no están almacenados en una colección, sino que se generan "on the fly". 
Un generador también se puede instanciar con una expresión entre paréntesis



'''

def pares(n):
    for numero in range(n+1):
        if numero%2 == 0:
            yield numero

pares(20)

for numero in pares(20):
    print(numero)


#funcion next
#next(cadena_iterable)

'''
Funciones generadoras
Crea una función generadora llamada cuadrados(numero) que a partir de un número genere todos los números de 1 a X (ambos incluidos) y sus potencias de dos.

Ejemplo de la conversión del generador a lista:

list(cuadrados(5))
Devolverá:

[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
Una lista con tuplas, cada tupla contiene el número y su cuadrado.

Notas:

Única y exclusivamente tienes que programar la función, no debe haber ningún otro código en el ejercicio.

No tienes que devolver la conversión a lista, solo el generador.

'''

# Completa el ejercicio
def cuadrados(numero):
    for i in range(1, numero+1):
        yield i, i**2