from cProfile import label
from tkinter import * 

root = Tk()
root.title("RadioButton")

r = IntVar()
r.set("2")

# variable = VariableAsignar, value = ValorAsignar
rBtn1 = Radiobutton(root, text="Opción 1", variable=r, value=1).pack()
Radiobutton(root, text="Opción 2", variable=r, value=2).pack()

l = Label(root, textvariable=r).pack()

root.mainloop()