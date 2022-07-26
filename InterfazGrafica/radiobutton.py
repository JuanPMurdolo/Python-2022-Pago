from tkinter import *

def select():
    monitor.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = IntVar()
Radiobutton(root, text="Opcion 1", variable=opcion, value=1, command=select).pack()
Radiobutton(root, text="Opcion 2", variable=opcion, value=2, command=select).pack()
Radiobutton(root, text="Opcion 3", variable=opcion, value=3, command=select).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()