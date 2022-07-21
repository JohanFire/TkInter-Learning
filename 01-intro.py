from tkinter import *

root =Tk()
root.title("Holis")
root.geometry("400x200") # dimensiones de la app (ANCHOxALTO)

# Forma 1 -----
label1 = Label(root, text="Hola Mundo!") # (root= renderizarse en root)
# con label.pack instanciamos/mostramos la label anteriormente creada
label1.pack()

# Forma 2 -----
# de esta manera se puede agregar una label y mostrarla con la misma línea de código, 
# aunque no se crea una variable, para futuros usos
Label(root, text="Esta es una 2da etiqueta, con .pack en la misma línea").pack()


# mainloop se queda escuchando a posibles cambios en main root
root.mainloop() 