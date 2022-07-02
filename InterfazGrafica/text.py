import imp
from tkinter import *

root = Tk()


texto = Text(root)
texto.pack()
texto.config(width=30, height=10, font=("Consolas",12), padx=5, pady=5, selectbackground="red")


root.mainloop()
