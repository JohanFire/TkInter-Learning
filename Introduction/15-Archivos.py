from tkinter import *
from tkinter import filedialog
# from PIL import ImageTk, Image

root = Tk()
root.title("Abrir archivos")

def openFile():
    root.filename = filedialog.askopenfilename(title="Elige un archivo", filetypes=(("Archivos PNG", "*.png"),
        ("Todos", "*")))
    lbl1 = Label(root, text=root.filename).pack()


Button(root, text="Seleccionar archivo", command=openFile).pack()

# img = Image.open(root.filename)
# imgTk = ImageTk(img)

# lbl2 = Label(root, image=imgTk)
# lbl2.pack()

root.mainloop()