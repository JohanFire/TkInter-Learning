from tkinter import *

root = Tk()
root.title("Label Frame")
# root.geometry("300x300")

# frame1 = Labelframe(root, text="Login", padx=20, pady=20, borderwidth=10)
frame1 = LabelFrame(root, padx=20, pady=20, borderwidth=10)
frame1.pack(padx=50, pady=50)

label1 = Label(frame1, text="Etiqueta 1")
label1.pack()

btn1 = Button(frame1, text="Salir", command=root.quit)
btn1.pack()

root.mainloop()