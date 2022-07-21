# transformar de pies a metros
from tkinter import *

root = Tk()
root.title("Pies a Metros")

def calcular(*args):
    try:
        value = float(pies.get())
        resultado = int(0.3048 * value * 10000 + 0.5)/10000
        metros.set(resultado)
    except ValueError:
        metros.set("ERROR")
    # logging.debug("Hola")

frame = Frame(root, pady=3, padx=12)
frame.grid(column=0, row=0)

pies = StringVar()
pies_input = Entry(frame, width=7, textvariable=pies)
pies_input.grid(column=1, row=0)

metros = StringVar()
# metros.set("valor")
Label(frame, textvariable=metros).grid(column=1, row=1)

Label(frame, text="pies").grid(column=3, row=0)
Label(frame, text="es igual a:").grid(column=0, row=1)
Label(frame, text="metros").grid(column=3, row=1)
Label(frame, text="").grid(column=0, row=3)

Button(frame, text="Calcular", command=calcular).grid(column=3, row=4)

pies_input.focus()

root.bind("<Return>", calcular) # mandar argumentos *args a la función calcular

root.mainloop()