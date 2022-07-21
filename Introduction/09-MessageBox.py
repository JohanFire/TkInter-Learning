# el método favorito es: messagebox.askokcancel()

from tkinter import *
from tkinter import messagebox 

root = Tk()
root.title("MessageBox")

def click(*args):
    messagebox.showwarning("PopUp", "messagebox.showwarning")
    messagebox.showinfo("PopUp", "messagebox.showinfo")
    messagebox.showerror("PopUp", "messagebox.showerror")
    
    respuesta = messagebox.askquestion("PopUp", "messagebox.askquestion")
    print(respuesta)

    if respuesta == "yes":
        messagebox.showinfo("Respuesta", "Tu respuesta fue: {}".format(respuesta))
    else:
        messagebox.showinfo("Respuesta", "Tu respuesta fue: " + respuesta)

def click2():
    # askokcancel retorna un BOOLEANO, por lo que el if puede ser if respuesta:
    respuesta = messagebox.askokcancel("Hola", "Desea realizar la acción?")
    if respuesta:
        messagebox.showinfo("Hola", "La respuesta fue OK")
    else:
        messagebox.showinfo("Hola", "La respuesta fue CANCELAR")

def click3():
    # muestra un OK cuando elegimos una opción
    respuesta = messagebox.askyesno("Hola", "Desea realizar la acción?")
    if respuesta:
        messagebox.showinfo("Hola", "La respuesta fue YES")
    else:
        messagebox.showinfo("Hola", "La respuesta fue NO")


btn1 = Button(root, text="Dame click", command=click).pack()
btn2 = Button(root, text="ask ok cancel", command=click2).pack()
btn3 = Button(root, text="ask yes no", command=click3).pack()

root.bind("<Return>", click)
root.mainloop()