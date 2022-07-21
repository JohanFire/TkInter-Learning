from tkinter import *

root = Tk()
root.title("Quit")

btnExit = Button(root, text="Salir", command=root.quit).pack()

root.mainloop()