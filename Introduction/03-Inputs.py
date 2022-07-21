from cProfile import label
from tkinter import *

root = Tk()
root.title("Inputs")
root.geometry("300x300")

input1 = Entry(root, width=60)
input1.pack()
input1.insert(0, "Ingresa texto: ")

def click():
    texto = input1.get()
    label1.configure(text = texto)

btn1 = Button(root, text="Click", command=click)
btn1.pack()

label1 = Label(root, text="Texto de etiqueta: ")
label1.pack()

# 
Label(root, text="").pack()
Label(root, text="").pack()
Label(root, text="").pack()

# 
input2 = Entry(root, width=60)
input2.pack()
input2.insert(0, "Input2: ")

def click2():
    texto = input2.get()
    label2 = Label(root, text=texto)
    label2.pack()
    input2.delete(0, END) #(desde el 0, hasta el final END)

btn2 = Button(root, text="Click 2", command=click2)
btn2.pack()



root.mainloop()