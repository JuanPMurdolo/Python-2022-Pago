#Editor de texto personalizado con funciones de guardado, apertura

from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = "" #global, almacena rutas de ficheros

def nuevo():
    global ruta
    mensaje.set("Nuevo Fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Editor personalizado")

def abrir():
    global ruta
    mensaje.set("Abrir Fichero")
    ruta = FileDialog.askopenfile(filetypes=".", filetype=(("Ficheros de texto", "*.txt"),), title="Abrir un fichero de texto")
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, "end")
        texto.insert("insert", contenido)
        fichero.close()
        root.title(ruta + " - Editor personalizado")

def guardar():
    global ruta
    mensaje.set("Guardar Fichero")
    if ruta != "":
        contenido = texto.get(1.0, "end-1c")
        fichero= open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardarComo()

def guardarComo():
    global ruta    
    mensaje.set("Guardar Fichero como")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, "end-1c")
        fichero= open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("guardado cancelado")
        ruta = ""


root = Tk()
root.title("Editor de texto personalizado")

#Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar Como", command=guardarComo)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

#Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))


#Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido al editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")


root.config(menu=menubar)
root.mainloop()