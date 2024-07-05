from tkinter import *
import random

rootmath = Tk()
rootmath.title("Математика")
pagemat = Frame(rootmath)

point = 0
res = 0
operation = ""

def sum():
    def back():
        label.grid_remove()
        text.grid_remove()
        but.grid_remove()
        butbk.grid_remove()
        butsum.grid(row=1, column=1)
        butsub.grid(row=2, column=1)
        butdiv.grid(row=3, column=1)
        butmul.grid(row=4, column=1)
    global res, operation
    operation = "sum"
    x = random.randrange(100, 1000)
    y = random.randrange(100, 1000)
    res = x + y
    label = Label(pagemat, text=f"{x} + {y}", width=20, height=1, font='arial 32')
    butbk = Button(pagemat, height=2, width=15, font='Arial 14', text="Назад", command=back)
    label.grid_remove()
    butsum.grid_remove()
    butsub.grid_remove()
    butdiv.grid_remove()
    butmul.grid_remove()
    label.grid(row=1,column=1)
    text.grid(row=2,column=1)
    but.grid(row=3,column=1)
    butbk.grid(row=4, column=1)

def sub():
    def back():
        label.grid_remove()
        text.grid_remove()
        but.grid_remove()
        butbk.grid_remove()
        butsum.grid(row=1, column=1)
        butsub.grid(row=2, column=1)
        butdiv.grid(row=3, column=1)
        butmul.grid(row=4, column=1)
    global res, operation
    operation = "sub"
    x = random.randrange(100, 1000)
    y = random.randrange(100, 1000)
    res = x - y
    label = Label(pagemat, text=f"{x} - {y}", width=20, height=1, font='arial 32')
    butbk = Button(pagemat, height=2, width=15, font='Arial 14', text="Назад", command=back)
    label.grid_remove()
    butsum.grid_remove()
    butsub.grid_remove()
    butdiv.grid_remove()
    butmul.grid_remove()
    label.grid(row=1,column=1)
    text.grid(row=2,column=1)
    but.grid(row=3,column=1)
    butbk.grid(row=4, column=1)

def div():
    def back():
        label.grid_remove()
        text.grid_remove()
        but.grid_remove()
        butbk.grid_remove()
        butsum.grid(row=1, column=1)
        butsub.grid(row=2, column=1)
        butdiv.grid(row=3, column=1)
        butmul.grid(row=4, column=1)
    global res, operation
    operation = "div"
    x = random.randrange(100, 1000, 2)
    y = random.randrange(2, 10, 2)
    res = x / y
    label = Label(pagemat, text=f"{x} / {y}", width=20, height=1, font='arial 32')
    butbk = Button(pagemat, height=2, width=15, font='Arial 14', text="Назад", command=back)
    label.grid_remove()
    butsum.grid_remove()
    butsub.grid_remove()
    butdiv.grid_remove()
    butmul.grid_remove()
    label.grid(row=1,column=1)
    text.grid(row=2,column=1)
    but.grid(row=3,column=1)
    butbk.grid(row=4, column=1)

def mul():
    def back():
        label.grid_remove()
        text.grid_remove()
        but.grid_remove()
        butbk.grid_remove()
        butsum.grid(row=1, column=1)
        butsub.grid(row=2, column=1)
        butdiv.grid(row=3, column=1)
        butmul.grid(row=4, column=1)
    global res, operation
    operation = "mul"
    x = random.randrange(10, 100)
    y = random.randrange(10, 100)
    res = x * y
    label = Label(pagemat, text=f"{x} * {y}", width=20, height=1, font='arial 32')
    butbk = Button(pagemat, height=2, width=15, font='Arial 14', text="Назад", command=back)
    label.grid_remove()
    butsum.grid_remove()
    butsub.grid_remove()
    butdiv.grid_remove()
    butmul.grid_remove()
    label.grid(row=1,column=1)
    text.grid(row=2,column=1)
    but.grid(row=3,column=1)
    butbk.grid(row=4, column=1)

def check():
    global res, point, operation
    answer = int(text.get('1.0', END))
    if answer == res:
        point += 1
        text.delete("1.0", END)
        if operation == "sum":
            sum()
        if operation == "sub":
            sub()
        if operation == "div":
            div()
        if operation == "mul":
            mul()

text = Text(pagemat,height=1,width=6,font='Arial 32')
but = Button(pagemat,height=2,width=15,font='Arial 14',text="Проверить", command=check)
butsum = Button(pagemat,height=2,width=15,font='Arial 14',text="Сложения", command=sum)
butsub = Button(pagemat,height=2,width=15,font='Arial 14',text="Вычитание", command=sub)
butdiv = Button(pagemat,height=2,width=15,font='Arial 14',text="Деление", command=div)
butmul = Button(pagemat,height=2,width=15,font='Arial 14',text="Умножение", command=mul)

def run():
    pagemat.grid()
    butsum.grid(row=1,column=1)
    butsub.grid(row=2,column=1)
    butdiv.grid(row=3,column=1)
    butmul.grid(row=4,column=1)
    rootmath.mainloop()