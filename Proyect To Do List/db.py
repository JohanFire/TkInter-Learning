from tkinter import *
import sqlite3

root = Tk()
root.title("DATA BASE: To Do List")
root.geometry("400x500")

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

def remove(id):
    def _remove():
        c.execute("DELETE FROM todo WHERE id = ?", (id, ))
        conn.commit()
        renderTodos()
    return _remove

# Currying! retrasar la aplicación de una función
def complete(id):
    def _complete():
        todo = c.execute("SELECT * from todo WHERE id = ?", (id, )).fetchone()
        c.execute("UPDATE todo SET completed = ? WHERE id = ?", (not todo[3], id)) # todo[3]4ta columna, el estado final
        conn.commit()
        renderTodos()
        print(id)
    return _complete
        

def renderTodos():
    rows = c.execute("SELECT * FROM todo").fetchall()
    print(rows)

    # eliminar elementos dentro del frame
    for widget in frame.winfo_children():
        widget.destroy( )

    for i in range(0, len(rows)):
        id = rows[i][0]
        completed = rows[i][3]
        description = rows[i][2]
        color = "#C4C3A3" if completed else "#141411"
        checkBtn = Checkbutton(frame, text=description, fg=color, width=42, anchor="w", 
        # Currying aplicado 
        command=complete(id))
        
        checkBtn.grid(row=i, column=0, sticky="w")
        checkBtn.select() if completed else checkBtn.deselect()

        btnEliminar = Button(frame, text="Eliminar", command=remove(id))
        btnEliminar.grid(row=i, column=1)

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