from tkinter import *

root = Tk()
'''
frame = Frame(root, width=480, height=320)
frame.pack()

texto= StraingVar()
texto.set("Un nuevo Texto")

label= Label(frame, text="Hola Mundo")
label.place(x=0, y=0)

Label(root, text="HolaMundo").pack(anchor="nw")
label = Label(root, text = "Otro")
label.pack(anchor="center")
Label(root,, text="Otra mas").pack(anchor="se")

label.config(bg="green", fg="blue", font=("Verdana",24))
label.config(textvariable=texto)
'''
img = PhotoImage(file="imagen.gif")
Label(root, image=img, bd=0).pack(side="left")

root.mainloop()