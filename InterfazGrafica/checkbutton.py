from tkinter import *

def select():
    cadena = ""
    if (leche.get()):
        cadena += "Con leche"
    else:
        cadena += "Sin leche"
    if (azucar.get()):
        cadena += " y con azucar"
    else:
        cadena += "  y sin azucar"
    monitor.config(text=cadena)

root = Tk()
root.title("Cafeteria")
root.config(bd=15)

leche = IntVar()
azucar = IntVar()


imagen = PhotoImage(file="/home/rednimbus/Documentos/GitHub/Python 2022 (Curso Pago)/Python-2022-Pago/InterfazGrafica/imagen.gif")
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="bottom")

Label(root, text="Como quieres el cafe?").pack(anchor="w")
Checkbutton(root, text="Con leche", variable = leche, onvalue=1, offvalue=0, command=select).pack(anchor="w")
Checkbutton(root, text="Con azucar", variable = azucar, onvalue=1, offvalue=0, command=select).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

root.mainloop()