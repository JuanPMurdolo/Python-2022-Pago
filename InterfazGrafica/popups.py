from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()

def test():
    MessageBox.showinfo("Hola","Mundo")

def test2():
    MessageBox.showwarning("ALERTA","ROJA")

def test3():
    MessageBox.showerror("ALERTA","Error inesperado")

def test4():
    resultado = MessageBox.askquestion("Seguro queres salir?","Seguro Seguro?")
    if resultado == "yes":
        root.destroy()

def test5():
    resultado = MessageBox.askokcancel("Seguro queres pisar el archivo?","Seguro Seguro?")
    if resultado:
        root.destroy()

def test6():
    resultado = MessageBox.askyesno("Seguro queres pisar el archivo?","Seguro Seguro?")
    if resultado:
        root.destroy()

def test7():
    resultado = MessageBox.askretrycancel("Seguro queres pisar el archivo?","Seguro Seguro?")
    if resultado:
        root.destroy()

def color():
    color = ColorChooser.askcolor(title="Elegi un color")
    print(color)

def fileDialog():
    ruta = FileDialog.askopenfile(title="abrir un fichero", 
        filetypes=(
        ("Ficheros de texto", "*.txt"),
        ("Todos los ficheros","*.*")
    ))
    print(ruta)

def fileDialog2():
    ruta = FileDialog.asksaveasfile(title="Guardar un fichero", mode="w+", defaultextension=".txt")
    if ruta is not None:
        ruta.write("HOla!")
        ruta.close()

Button(root, text="Hazme Click", command=test).pack()
Button(root, text="Hazme Click 2", command=test2).pack()
Button(root, text="Hazme Click 3", command=test3).pack()
Button(root, text="Hazme Click 4", command=test4).pack()
Button(root, text="Hazme Click 5", command=test5).pack()
Button(root, text="Hazme Click 6", command=test6).pack()
Button(root, text="Hazme Click 7", command=test7).pack()
Button(root, text="color", command=color).pack()
Button(root, text="fileDialog", command=fileDialog).pack()
Button(root, text="fileDialog Save", command=fileDialog2).pack()
root.mainloop()