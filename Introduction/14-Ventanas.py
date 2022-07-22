from tkinter import *

root = Tk()
root.title("Windows")

def openWindow():
    top = Toplevel()
    top.title("Nueva Ventana")
    Label(top, text="Holis, texto de ventana 'top'").pack()
    
    top.mainloop()

btn1 = Button(root, text="Abrir otra Ventana", command=openWindow).pack()

root.mainloop()