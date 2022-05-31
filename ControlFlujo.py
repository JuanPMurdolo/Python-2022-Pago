"""1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción válida, el programa informará de que no es correcta.
"""
numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))
menu = int(input("Elija una opcion: 1 para sumas, dos para restas, 3 para multiplicacion: "))
if menu == 1:
    print(numero1 + numero2)
elif menu == 2:
    print(numero1 - numero2)
elif menu == 3:
    print(numero1 * numero2)
else:
    print("opcion incorrecta")
"""
2) Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.
"""
condicion = False
while condicion == False:
    numero1 = int(input("Ingresa un numero impar: "))
    if numero1 % 2 != 0:
        print("Numero correcto")
        condicion = True
    else:
        print("Error intente de nuevo")
"""
3) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:
Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.
"""
lista = []
for i in range(0,100,2):
    lista.append(i)
print(sum(lista))
"""
4) Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:
"""
suma = 0
numerosIngresar = int(input("cuanto numeros desea ingresar: "))
for i in range(numerosIngresar):
    num = int(input("ingrese numero: "))
    suma = suma + num
    i += 1
print("La media aritmetica es:", suma / numerosIngresar)
"""
5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

Consejo: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)
"""
numeros = [1, 3, 6, 9]
condicion = False
while condicion == False:
    numero1 = int(input("Ingresa un numero: "))
    for i,num in enumerate(numeros):
        if numero1 == numeros[i]:
            condicion = True

"""
6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
Pista: Utiliza el tercer parámetro de la función range(inicio, fin, salto).
"""
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []

for i in range(0,11,1):
    lista1.append(i)
for i in range(-10,1,1):
    lista2.append(i)
for i in range(0,21,2):
    lista3.append(i)
for i in range(-20,1,1):
    if i % 2 != 0:
        lista4.append(i)
for i in range(0,51,5):
    lista5.append(i)
print(lista1, lista2, lista3, lista4, lista5)

"""
7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetise ningún elemento en la nueva lista:
"""
lista1 = [1,2,3,4,5,6,7,8,9,10,11]
lista2 = [1,3,5,7,9,11]
lista3 = []

for i,item in enumerate(lista1):
    for j, item2 in enumerate(lista2):
        if lista1[i] == lista2[j]:
            lista3.append(lista1[i])
print(lista3)
