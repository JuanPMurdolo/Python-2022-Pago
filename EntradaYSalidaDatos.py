'''
1) Formatea los siguientes valores para mostrar el resultado indicado:

"Hola Mundo" → Alineado a la derecha en 20 caracteres
"Hola Mundo" → Truncamiento en el cuarto carácter (índice 3)
"Hola Mundo" → Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)
150 → Formateo a 5 números enteros rellenados con ceros
7887 → Formateo a 7 números enteros rellenados con espacios
20.02 → Formateo a 3 números enteros y 3 números decimales
'''
# Completa el ejercicio aquí
print( "{:>20}".format("Hola Mundo") )
print( "{:.3}".format("Hola Mundo") )
print( "{:^20.2}".format("Hola Mundo") )
print( "{:05d}".format(150) )
print( "{:7d}".format(7887) )
print( "{:07.3f}".format(20.02) )

'''
2) Crea un script llamado tabla.py que realice las siguientes tareas:

Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
El script contendrá un bucle for que itere el número de veces del primer argumento.
Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
Dentro del segundo for ejecuta una instrucción ** print(" * ", end='')**, (end='' evita el salto de línea).
Ejecuta el código y observa el resultado.
** Ahora intenta deducir dónde y cómo añadir otra instruccion print para dibujar una tabla.**

Recordatorio: Los argumentos se envían como cadenas separadas por espacios, si quieres enviar varias palabras como un argumento deberás indicarlas entre comillas dobles "esto es un argumento". Para capturar los argumentos debes utilizar el módulo sys y su lista argv:

import sys
print(sys.argv) # argumentos enviados
'''

#Tabla.py
import sys
if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print("Error - Filas o columnas incorrectos")
        print("Ejemplo: tabla.py [1-9] [1-9]")
    else:
        # Aqui empieza la lógica
        for f in range(filas):
            print("")
            for c in range(columnas):
                print(" * ", end='')
else:
    print("Error - Argumentos incorrectos")
    print("Ejemplo: tabla.py [1-9] [1-9]")

'''
3) [Avanzado] Crea un script llamado descomposicion.py que realice las siguientes tareas:

Debe tomar 1 argumento que será un número entero positivo.
En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
** El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:**

> 3647
** El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo: **

> 0007
  0040
  0600
  3000
Pista: Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa
'''
import sys
if len(sys.argv) == 1:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print("Error - Número es incorrecto")
        print("Ejemplo: descomposicion.py [0-9999]")
    else:
        # Aqui va la lógica
        cadena = str(numero)
        longitud = len(cadena)

        for i in range(longitud):
            print( "{:04d}".format( int(cadena[longitud-1-i]) * 10 ** i ))
else:
    print("** El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:**")
    print("3647")
    print("** El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo: **")
    print("0007")
    print("0040")
    print("0600")
    print("3000")