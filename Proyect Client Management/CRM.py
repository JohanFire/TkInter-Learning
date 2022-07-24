from email import message
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

from pynvim import command

root = Tk()
root.title("Client Management")

# DB Connection
conn = sqlite3.connect("Proyect Client Management/CRM.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE if not exists crm (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        name TEXT NOT NULL,
        telephone TEXT NOT NULL,
        brand TEXT NOT NULL
    );
""")
conn.commit()

# Interface
def new_Client():
    top = Toplevel()
    top.title("Nuevo cliente")

    def save():
        pass

    lblName = Label(top, text="Nombre")
    lblName.grid(row=0, column=0)
    inputName = Entry(top, width=40)
    inputName.grid(row=0, column=1)

    lblTel = Label(top, text="Teléfono")
    lblTel.grid(row=1, column=0)
    inputTel = Entry(top, width=40)
    inputTel.grid(row=1, column=1)

    lblBrand = Label(top, text="Brand")
    lblBrand.grid(row=2, column=0)
    inputBrand = Entry(top, width=40)
    inputBrand.grid(row=2, column=1)

    btnSave = Button(top, text="Guardar", command=save)
    btnSave.grid(row=3, column=1)

    top.mainloop()

def delete_Client():
    answer = messagebox.askokcancel("Eliminar cliente", "¿Estás seguro de querer eliminar a este cliente?")
    if answer:
        messagebox.showinfo("Cliente eliminado", "El cliente ha sido elimiando correctamente")
    else:
        pass

btnNewClient = Button(root, text="Nuevo Client", command=new_Client)
btnNewClient.grid(column=0, row=0)

btnDelete = Button(root, text="Eliminar Cliente", command=delete_Client)
btnDelete.grid(column=1, row=0)

tree = ttk.Treeview(root)
tree["columns"] = ("Nombre", "Telefono", "Empresa")
tree.column("#0", width=0, stretch=NO)
tree.column("Nombre")
tree.column("Telefono")
tree.column("Empresa")

tree.heading("Nombre", text="Nombre")
tree.heading("Telefono", text="Teléfono")
tree.heading("Empresa", text="Empresa")
tree.grid(column=0, row=1, columnspan=2)

tree.insert("", END, "lala", values=("Uno", "Dos", "Tres"), text="chanchito")

root.mainloop()