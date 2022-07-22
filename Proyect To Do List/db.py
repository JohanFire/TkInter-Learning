from tkinter import *
import sqlite3

root = Tk()
root.title("DATA BASE: To Do List")
root.geometry("500x500")

myConnection = sqlite3.connect("todo.db")

c = myConnection.cursor()

c.execute(""" 
    CREATE TABLE if not exists todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    );
""")

myConnection.commit()

root.mainloop()