from tkinter import *
import tkinter as tk
# win = window
win = tk.Tk()
win.title("Calculator")
win.geometry("540x600")
win.resizable(False,False)
win.configure(background="grey")

equation = ""

def show(value):
    global equation
    equation+=value
    label_display.config(text = equation)

def clear():
    global equation
    equation = ""
    label_display.config(text = equation)

def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result = eval(equation)
        except:
            result = "Can not divide by Zero."
            equation = ""
    label_display.config(text = result)

def back(value):
    global equation
    equation = equation[1:]
    label_display.config(text = equation)
    

label_display = Label(win, width=24, height=2, text="", font=("Calibri",30), bg="grey",relief=SUNKEN)
label_display.pack()

Button(win, text="C", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="red", command = lambda: clear()).place(x=30, y=110)
Button(win, text="/", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("/")).place(x=160, y=110)
Button(win, text="%", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("%")).place(x=280, y=110)
Button(win, text="*", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("*")).place(x=400, y=110)

Button(win, text="7", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("7")).place(x=30, y=210)
Button(win, text="8", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("8")).place(x=160, y=210)
Button(win, text="9", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("9")).place(x=280, y=210)
Button(win, text="-", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("-")).place(x=400, y=210)

Button(win, text="4", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("4")).place(x=30, y=310)
Button(win, text="5", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("5")).place(x=160, y=310)
Button(win, text="6", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("6")).place(x=280, y=310)
Button(win, text="+", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("+")).place(x=400, y=310)

Button(win, text="1", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("1")).place(x=30, y=410)
Button(win, text="2", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("2")).place(x=160, y=410)
Button(win, text="3", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("3")).place(x=280, y=410)
Button(win, text="=", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: calculate()).place(x=400, y=410)

Button(win, text="back", width=11, height=1, font=("Calibri",30), bd=1, fg="white", bg="red", command = lambda: back(equation)).place(x=280, y=510)

Button(win, text="0", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show("0")).place(x=30, y=510)
Button(win, text=".", width=5, height=1, font=("Calibri",30), bd=1, fg="white", bg="black", command = lambda: show(".")).place(x=160, y=510)


win.mainloop()











































