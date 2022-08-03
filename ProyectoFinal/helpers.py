import os
import platform
import re

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def leer_texto(msj=None, min=0, max=100):
    print(msj) if msj else None
    while True:
        texto = input("> ")
        if len(texto) >= min and len(texto) <= max:
            return texto

def validar_dni(dni, lista):
    if not re.match('[0-9]', dni):
        print("DNI incorrecto debe cumplir el formato")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI ya existe")
            return False
    return True
