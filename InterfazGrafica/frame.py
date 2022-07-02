from tkinter import *
import tkinter

root = Tk()
root.title("Test")
root.iconbitmap("@hola.xbm")
#img = PhotoImage(file="hola.xbm")  # Replace "image.png" with any image file.
#root.iconphoto(True, img)
#img = tkinter.Image("photo", file="test.png")
#root.tk.call('wm','iconphoto',root._w,img)
root.resizable(True, True)

frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1)
frame.config(cursor = "pirate")
frame.config(bg="lightblue")
frame.config(bd=20)
frame.config(relief="sunken")



root.config(cursor = "arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")


root.mainloop()
