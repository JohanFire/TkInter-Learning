from tkinter import * 

root = Tk()
root.title("Buttons")
root.geometry("300x300")

label1 = Label(root, text="Este texto sólo se puede agregar 1 vez")
def click():
    label1.pack()

btn1 = Button(root, text="Click", command=click)
btn1.pack()

# 
def click2():
    label2 = Label(root, text="Este texto se agrega infinitamente")
    label2.pack()

# el color soporta código hexadecimal
btn2 = Button(root, text="Click 2", command=click2, fg="#ff0000", bg="white")
btn2.pack()


root.mainloop()