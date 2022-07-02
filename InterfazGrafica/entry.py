from tkinter import *

root = Tk()

label = Label(root, text="Nombre  ")
label.grid(row=0, column=0, sticky="e", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0,column=1, padx=5, pady=5)

label2 = Label(root, text="Apellidos")
label2.grid(row=1, column=0, sticky="e", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()