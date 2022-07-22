from tkinter import *

root = Tk()
root.title("Slide")

# Forma tradicional, se actualiza hasta presionar botón
# slideVertical = Scale(root, from_=0, to=200)

# Forma chevere, se actualiza el valor en tiempo real sin necesidad de presionar el botón
slideVertical = Scale(root, from_=0, to=200, command=lambda x: enviar())
slideVertical.pack()

slideHorizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
slideHorizontal.pack()

def enviar():
    hor = slideHorizontal.get()
    ver = slideVertical.get()
    print(str(hor) + " " + str(ver))

btn = Button(root, text="Enviar", command=enviar).pack()

root.mainloop()