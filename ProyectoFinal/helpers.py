import os
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def leer_texto(msj=None, min=0, max=100):
    print(msj) if msj else None
    while True:
        texto = input("> ")
        if len(texto) >= min and len(texto) <= max:
            return texto
