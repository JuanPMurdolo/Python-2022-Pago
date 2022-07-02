from os import stat
from tkinter import *

def hola():
    print("Hola")

def crear_label():
    Label(root, text="Label creada dinamicamente").pack()

def sumar():
    r.set(float(n1.get())+float(n2.get()))
    borrar()

def borrar():
    n1.set("")
    n2.set("")

root = Tk()
root.config(bd=15)
Button(root, text="Click", command=crear_label).pack()


#Suma
Label(root, text="SUMA").pack()
n1 = StringVar()
n2 = StringVar()
r = StringVar()
Label(root, text="Numero 1").pack()
Entry(root, justify="center", textvariable=n1).pack()
Label(root, text="Numero 2").pack()
Entry(root, justify="center", textvariable=n2).pack()
Label(root, text="\nResultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()
Label(root, text="  ")
Button(root, text="Sumar", command=sumar).pack()

root.mainloop()