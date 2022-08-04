"""
**1) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:**
"""
try:
    resultado = 10/0
except:
    print("No se puede dividir por 0")

"""
2) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
"""
# Completa el ejercicio aquí
lista = [1, 2, 3, 4, 5]
try: 
    lista[10]
except:
    print("El index no puede ser mayor a la longitud de la lista")

"""
3) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
"""
# Completa el ejercicio aquí
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
try:
    colores['blanco']
except:
    print("No existe el color blanco")

"""
4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
"""
# Completa el ejercicio aquí
try:
    resultado = 15 + "20"
except:
    print("no se puede sumar tipo String")
"""
5) Realiza una función llamada agregar_una_vez() que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:

  Error: Imposible añadir elementos duplicados => [elemento].
** Prueba de agregar los elementos 10, -2, "Hola" a la lista de elementos con la función una vez la has creado y luego muestra su contenido.**

Nota: Puedes utilizar la sintaxis: elemento in lista
"""

elementos = [1, 5, -2]

# Completa el ejercicio aquí
def agregar_una_vez(lista, elemento):
    try:
        if elemento in lista:
            raise ValueError
        else:
            lista.append(elemento)
    except ValueError:
        print("Error: Imposible añadir elementos duplicados =>", elemento)
        

agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")
print(lista)