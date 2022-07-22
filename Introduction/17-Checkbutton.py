from tabnanny import check
from tkinter import * 

root = Tk()
root.title("Checkbuttons")
root.geometry("500x500")

var = StringVar()
var.set("no")

def mostrar():
    lbl1 = Label(root, text=var.get())
    lbl1.pack()

checkBtn1 = Checkbutton(root, text="Soy un Checkbutton", variable=var, onvalue="si", offvalue="no")
checkBtn1.pack()

btn1 = Button(root, text="Click", command=mostrar)
btn1.pack()


root.mainloop()