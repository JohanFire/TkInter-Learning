from tkinter import *

root = Tk()
root.title("OptionMenu / DropDown")
root.geometry("500x500")

def enviar():
    lbl1 = Label(root, text=val.get())
    lbl1.pack

lista = [
    "Chanchito", 
    "Feliz", 
    "Triste"
]

val = StringVar()
val.set(lista[1]) 

dropD = OptionMenu(root, val, *lista)
dropD.pack()

btn1 = Button(root, text="Enviar", command=enviar)
btn1.pack()

root.mainloop()