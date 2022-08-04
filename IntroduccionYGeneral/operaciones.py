#Modulo Operaciones
'''
El módulo se denominará operaciones y contendrá 4 funciones para realizar una suma, una resta, un producto y una division entres dos números. Todas ellas devolverán el resultado.
En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:
TypeError: En caso de que se envíen valores a las funciones que no sean números. Además deberá aparecer un mensaje que informe "Error: Tipo de dato no válido".
ZeroDivisionError: En caso de realizar una división por cero. Además deberá aparecer un mensaje que informe "Error: No es posible dividir entre cero".
'''

def suma(a,b):
    try:
        r = a + b
    except TypeError:
        print("Error: Tipo de dato no válido")
    else:
        return r


def resta(a,b):
    try:
        r = a - b
    except TypeError:
        print("Error: Tipo de dato no válido")
    else:
        return r


def producto(a,b):
    try:
        r = a * b
    except TypeError:
        print("Error: Tipo de dato no válido")
    else:
        return r


def division(a,b):
    try:
        r = a / b
    except TypeError:
        print("Error: Tipo de dato no válido")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
    else:
        return r