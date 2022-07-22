import imp
from optparse import Option
from tkinter import *

root = Tk()
root.title("OptionMenu / DropDown")
root.geometry("500x500")

val = StringVar()
val.set("Feliz") # dentro escribir el valor seteado por defecto

dropD = OptionMenu(root, val, "Chanchito", "Feliz", "Triste")
dropD.pack()

root.mainloop()