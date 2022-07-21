from tkinter import *
# Solo usuarios de MAC
# Para que la app se vea igual en Mac y en Windows
# pip3 install tkmacosx
# from tkmacosx import Button

root = Tk()
root.title("Calculadora")
# root.geometry("386x168")
root.configure(background="#333333")

equation = StringVar()

def press(num):
    print(num)
    equation.set(equation.get() + str(num))
    print(equation.get())

def equalPress():
    try:
        # eval, toma el string y trata de resolver la ecuasión
        total = str(eval(equation.get()))
        equation.set(total)
    except ValueError:
        equation.set("ERROR")

def clear():
    equation.set("")

expression_entry = Entry(root, textvariable=equation)
expression_entry.grid(row=0, columnspan=4, sticky="nswe") # (columnspan) será de 4 columnas pero si hay menos se mostrará menos

btn7 = Button(root, text="    7    ", fg="#fff", background="#666", command=lambda: press(7)).grid(row=1, column=0, sticky="nswe")
btn8 = Button(root, text="    8    ", fg="#fff", background="#666", command=lambda: press(8)).grid(row=1, column=1, sticky="nswe")
btn9 = Button(root, text="    9    ", fg="#fff", background="#666", command=lambda: press(9)).grid(row=1, column=2, sticky="nswe")

btn4 = Button(root, text="    4    ", fg="#fff", background="#666", command=lambda: press(4)).grid(row=2, column=0, sticky="nswe")
btn5 = Button(root, text="    5    ", fg="#fff", background="#666", command=lambda: press(5)).grid(row=2, column=1, sticky="nswe")
btn6 = Button(root, text="    6    ", fg="#fff", background="#666", command=lambda: press(6)).grid(row=2, column=2, sticky="nswe")

btn1 = Button(root, text="    1    ", fg="#fff", background="#666", command=lambda: press(1)).grid(row=3, column=0, sticky="nswe")
btn2 = Button(root, text="    2    ", fg="#fff", background="#666", command=lambda: press(2)).grid(row=3, column=1, sticky="nswe")
btn3 = Button(root, text="    3    ", fg="#fff", background="#666", command=lambda: press(3)).grid(row=3, column=2, sticky="nswe")

btn0 = Button(root, text="    0    ", fg="#fff", background="#666", command=lambda: press(0)).grid(row=4, column=0, sticky="nswe", columnspan=2)
btnDecimal = Button(root, text="   .   ", fg="#fff", background="#666", command=lambda: press(".")).grid(row=4, column=2, sticky="nswe")

btnPlus = Button(root, text="    +    ", fg="#fff", background="#fe9727", command=lambda: press("+")).grid(row=1, column=3, sticky="nswe")
btnMinus = Button(root, text="    -    ", fg="#fff", background="#fe9727", command=lambda: press("-")).grid(row=2, column=3, sticky="nswe")
btnMultiply = Button(root, text="    *    ", fg="#fff", background="#fe9727", command=lambda: press("*")).grid(row=3, column=3, sticky="nswe")
btnDivision = Button(root, text="    /    ", fg="#fff", background="#fe9727", command=lambda: press("/")).grid(row=4, column=3, sticky="nswe")

btnRes = Button(root, text="    =    ", fg="#fff", background="#fe9727", command=equalPress).grid(row=5, column=3, sticky="nswe")
btnClear = Button(root, text=" Clear ", fg="#fff", background="#666", command=clear).grid(row=5, column=2, sticky="nswe")



expression_entry.focus()

# root.bind("<Return>", funcion)
root.mainloop()