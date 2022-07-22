from tkinter import *
import sqlite3

root = Tk()
root.title("DATA BASE: To Do List")
root.geometry("350x500")

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

# Interface 
def renderTodos():
    rows = c.execute("SELECT * FROM todo").fetchall()
    print(rows)

    for i in range(0, len(rows)):
        isCompleted = rows[i][3]
        description = rows[i][2]
        checkBtn = Checkbutton(frame, text=description, width=42, anchor="w")
        checkBtn.grid(row=i, column=0, sticky="w")

def addTodo():
    todo = inputTarea.get()
    if todo:
        c.execute("""
            INSERT INTO todo (description, completed) VALUES (?, ?)
        """, (todo, False))
        conn.commit()
        inputTarea.delete(0, END)
        
        renderTodos()
    else:
        pass


lbl1 = Label(root, text="Tarea:")
lbl1.grid(row=0, column=0)

inputTarea = Entry(root, width=40)
inputTarea.grid(row=0, column=1)

btnAdd = Button(root, text="Agregar", command=addTodo)
btnAdd.grid(row=0, column=2)

frame = LabelFrame(root, text="Mis Tareas:", padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky="nswe", padx=5)

inputTarea.focus()


# la función manda un evento en un argumento, pero el argumento no me sirve de nada
# así que para no mandar ningún argumento, usé la función lambda
root.bind("<Return>", lambda x: addTodo())

renderTodos()

root.mainloop()