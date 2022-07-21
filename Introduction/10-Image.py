# pip install pillow
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image")

# imagen = Image.open("imagen.png")
# imagen.show()

# Forma preferida para trabajar con imagenes en TkInter
img = ImageTk.PhotoImage(Image.open("imagen.png"))
lab = Label(image=img)
lab.pack()

root.mainloop()