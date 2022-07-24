from tkinter import *
from tkinter import ttk

root = Tk()
root.title("TreeView")

tree = ttk.Treeview()
tree["columns"] = ("Nombre", "Teléfono", "Empresa")

# especificar índices de las columnas
tree.column("#0", width=0, stretch=NO)
# tree.column("#0")
tree.column("Nombre")
tree.column("Teléfono")
tree.column("Empresa")

# texto a mostrar dentro del head la columna
tree.heading("#0", )
# tree.heading("#0", text="id")
tree.heading("Nombre", text="Nombre")
tree.heading("Teléfono", text="Teléfono")
tree.heading("Empresa", text="Empresa")

tree.grid(row=0, column=0)

# string vacío ("") significa indicar en la base del árbol
tree.insert("", END, "lala", values=("Uno", "Dos", "Tres"), text="chanchito")
tree.insert("", END, "lele", values=("4", "cinco", "6"), text="chanchito2")
# tree.insert("lele", END, "lili", values=("7", "8", "9"), text="hijo")
tree.insert("", END, "lili", values=("7", "8", "9"), text="hijo")


root.mainloop()