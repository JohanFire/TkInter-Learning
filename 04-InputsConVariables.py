# esta es una mejor manera para manipular texto en los Entrys, usando variables

from tkinter import *

root = Tk()
root.title("Inputs con Variables")
root.geometry("300x300")

# 
Label(root, text="").pack()

# 
input2 = Entry(root, width=60)
input2.pack()
input2.insert(0, "Input2: ")

def click2():
    texto = input2.get()
    textoVar3.set(texto)
    valor = textoVar3.get()
    print(valor)
    # label2 = Label(root, text=texto)
    # label2.pack()
    input2.delete(0, END) 

btn2 = Button(root, text="Click 2", command=click2)
btn2.pack()

textoVar3 = StringVar()
label3 = Label(root, textvariable=textoVar3)
label3.pack()



root.mainloop()