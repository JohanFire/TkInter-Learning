from tkinter import *

root = Tk()
root.title("Sistema de Grillas")
root.geometry("500x300")

label1 = Label(root, text="Etiqueta 1")
label2 = Label(root, text="Etiqueta 2")
# label1.pack()
# label2.pack()

label3 = Label(root, text="                 ")
# label3.pack()

# para usar el GRID, se reemplaza el .pack()
label1.grid(row=0, column=0)
label3.grid(row=1, column=1)
label2.grid(row=10, column=10)



root.mainloop()