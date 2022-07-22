from tkinter import *
import sqlite3
from tkinter.ttk import Labelframe

root = Tk()
root.title("DATA BASE: To Do List")
root.geometry("500x500")

# DB Connection
conn = sqlite3.connect("Proyect To Do List/todo.db")
c = conn.cursor()

c.execute(""" 
    CREATE TABLE if not exists todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    );
""")
conn.commit()

# Creating Interface 

def addTodo():
    todo = inputTarea.get()
    c.execute("""
        INSERT INTO todo (description, completed) VALUES (?, ?)
    """, (todo, False))
    inputTarea.delete(0, END)


lbl1 = Label(root, text="Tarea:").grid(row=0, column=0)

inputTarea = Entry(root, width=40)
inputTarea.grid(row=0, column=1)

btnAdd = Button(root, text="Agregar", command=addTodo).grid(row=0, column=2)

frame = LabelFrame(root, text="Mis Tareas:", padx=5, pady=5).grid(row=1, column=0, columnspan=3,
    sticky="nswe", padx=5)

inputTarea.focus()

# la función manda un evento en un argumento, pero el argumento no me sirve de nada
# así que para no mandar ningún argumento, usé la función lambda
root.bind("<Return>", lambda x: addTodo())

root.mainloop()