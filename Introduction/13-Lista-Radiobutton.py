from tkinter import * 

root = Tk()
root.title("Lista Radiobuttons")

r = IntVar()
r.set("2")

chanchitos = [
    ("Feliz", "Feliz"),
    ("Triste", "Triste"),
    ("Amargado", "Amargado"),
    ("Wolfgang", "Wolfgang"),
]

chanchito = StringVar()
chanchito.set("Wolfgang")
for text, chancho in chanchitos:
    Radiobutton(root, text = text, variable=chanchito, value=chancho).pack()


lbl = Label(root, textvariable=chanchito).pack()

root.mainloop()