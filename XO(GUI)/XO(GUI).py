from tkinter import *
from threading import Thread

root = Tk()
page1 = Frame(root)
page2 = Frame(root)
f1 = "1"
f2 = "2"
f3 = "3"
f4 = "4"
f5 = "5"
f6 = "6"
f7 = "7"
f8 = "8"
f9 = "9"
hooismove = "X"

def b1():
    global f1, hooismove
    if hooismove == "X":
        f1 = "X"
        but1.grid_remove()
        butX1.grid(row=1, column=1)
        hooismove = "O"
    else:
        f1 = "O"
        but1.grid_remove()
        butO1.grid(row=1, column=1)
        hooismove = "X"

def b2():
    global f2, hooismove
    if hooismove == "X":
        f2 = "X"
        but2.grid_remove()
        butX2.grid(row=1, column=2)
        hooismove = "O"
    else:
        f2 = "O"
        but2.grid_remove()
        butO2.grid(row=1, column=2)
        hooismove = "X"


def b3():
    global f3, hooismove
    if hooismove == "X":
        f3 = "X"
        but3.grid_remove()
        butX3.grid(row=1, column=3)
        hooismove = "O"
    else:
        f3 = "O"
        but1.grid_remove()
        butO3.grid(row=1, column=3)
        hooismove = "X"

def b4():
    global f4, hooismove
    if hooismove == "X":
        f4 = "X"
        but4.grid_remove()
        butX4.grid(row=2, column=1)
        hooismove = "O"
    else:
        f4 = "O"
        but4.grid_remove()
        butO4.grid(row=2, column=1)
        hooismove = "X"

def b5():
    global f5, hooismove
    if hooismove == "X":
        f5 = "X"
        but5.grid_remove()
        butX5.grid(row=2, column=2)
        hooismove = "O"
    else:
        f5 = "O"
        but5.grid_remove()
        butO5.grid(row=2, column=2)
        hooismove = "X"

def b6():
    global f6, hooismove
    if hooismove == "X":
        f6 = "X"
        but6.grid_remove()
        butX6.grid(row=2, column=3)
        hooismove = "O"
    else:
        f6 = "O"
        but6.grid_remove()
        butO6.grid(row=2, column=3)
        hooismove = "X"

def b7():
    global f7, hooismove
    if hooismove == "X":
        f7 = "X"
        but7.grid_remove()
        butX7.grid(row=3, column=1)
        hooismove = "O"
    else:
        f7 = "O"
        but7.grid_remove()
        butO7.grid(row=3, column=1)
        hooismove = "X"

def b8():
    global f8, hooismove
    if hooismove == "X":
        f8 = "X"
        but8.grid_remove()
        butX8.grid(row=3, column=2)
        hooismove = "O"
    else:
        f8 = "O"
        but8.grid_remove()
        butO8.grid(row=3, column=2)
        hooismove = "X"

def b9():
    global f9, hooismove
    if hooismove == "X":
        f9 = "X"
        but9.grid_remove()
        butX9.grid(row=3, column=3)
        hooismove = "O"
    else:
        f9 = "O"
        but9.grid_remove()
        butO9.grid(row=3, column=3)
        hooismove = "X"


def winncomb():
    if f1 == "X" and f2 == "X" and f3 == "X":
        return 1
    elif f4 == "X" and f5 == "X" and f6 == "X":
        return 1
    elif f7 == "X" and f8 == "X" and f9 == "X":
        return 1
    elif f1 == "X" and f4 == "X" and f7 == "X":
        return 1
    elif f2 == "X" and f5 == "X" and f8 == "X":
        return 1
    elif f3 == "X" and f6 == "X" and f9 == "X":
        return 1
    elif f1 == "X" and f5 == "X" and f9 == "X":
        return 1
    elif f3 == "X" and f5 == "X" and f7 == "X":
        return 1
    elif f1 == "O" and f2 == "O" and f3 == "O":
        return 2
    elif f4 == "O" and f5 == "O" and f6 == "O":
        return 2
    elif f7 == "O" and f8 == "O" and f9 == "O":
        return 2
    elif f1 == "O" and f4 == "O" and f7 == "O":
        return 2
    elif f2 == "O" and f5 == "O" and f8 == "O":
        return 2
    elif f3 == "O" and f6 == "O" and f9 == "O":
        return 2
    elif f1 == "O" and f5 == "O" and f9 == "O":
        return 2
    elif f3 == "O" and f5 == "O" and f7 == "O":
        return 2

def again():
    page2.grid_remove()
    butX1.grid_remove()
    butX2.grid_remove()
    butX3.grid_remove()
    butX4.grid_remove()
    butX5.grid_remove()
    butX6.grid_remove()
    butX7.grid_remove()
    butX8.grid_remove()
    butX9.grid_remove()
    butO1.grid_remove()
    butO2.grid_remove()
    butO3.grid_remove()
    butO4.grid_remove()
    butO5.grid_remove()
    butO6.grid_remove()
    butO7.grid_remove()
    butO8.grid_remove()
    butO9.grid_remove()
    global f1, f2, f3, f4, f5, f6, f7, f8, f9
    f1 = "1"
    f2 = "2"
    f3 = "3"
    f4 = "4"
    f5 = "5"
    f6 = "6"
    f7 = "7"
    f8 = "8"
    f9 = "9"
    page1.grid()
    but1.grid(row=1, column=1)
    but2.grid(row=1, column=2)
    but3.grid(row=1, column=3)
    but4.grid(row=2, column=1)
    but5.grid(row=2, column=2)
    but6.grid(row=2, column=3)
    but7.grid(row=3, column=1)
    but8.grid(row=3, column=2)
    but9.grid(row=3, column=3)
    main()

but1 = Button(page1, text = f1, font='arial 60', width=2, height=2, command=b1)
but2 = Button(page1, text = f2, font='arial 60', width=2, height=2, command=b2)
but3 = Button(page1, text = f3, font='arial 60', width=2, height=2, command=b3)
but4 = Button(page1, text = f4, font='arial 60', width=2, height=2, command=b4)
but5 = Button(page1, text = f5, font='arial 60', width=2, height=2, command=b5)
but6 = Button(page1, text = f6, font='arial 60', width=2, height=2, command=b6)
but7 = Button(page1, text = f7, font='arial 60', width=2, height=2, command=b7)
but8 = Button(page1, text = f8, font='arial 60', width=2, height=2, command=b8)
but9 = Button(page1, text = f9, font='arial 60', width=2, height=2, command=b9)
butX1 = Button(page1, text="X", font='arial 60', width=2, height=2)
butX2 = Button(page1, text="X", font='arial 60', width=2, height=2)
butX3 = Button(page1, text="X", font='arial 60', width=2, height=2)
butX4 = Button(page1, text="X", font='arial 60', width=2, height=2)
butX5 = Button(page1, text="X", font='arial 60', width=2, height=2)
butX6 = Button(page1, text="X", font='arial 60', width=2, height=2)
butX7 = Button(page1, text="X", font='arial 60', width=2, height=2)
butX8 = Button(page1, text="X", font='arial 60', width=2, height=2)
butX9 = Button(page1, text="X", font='arial 60', width=2, height=2)
butO1 = Button(page1, text="O", font='arial 60', width=2, height=2)
butO2 = Button(page1, text="O", font='arial 60', width=2, height=2)
butO3 = Button(page1, text="O", font='arial 60', width=2, height=2)
butO4 = Button(page1, text="O", font='arial 60', width=2, height=2)
butO5 = Button(page1, text="O", font='arial 60', width=2, height=2)
butO6 = Button(page1, text="O", font='arial 60', width=2, height=2)
butO7 = Button(page1, text="O", font='arial 60', width=2, height=2)
butO8 = Button(page1, text="O", font='arial 60', width=2, height=2)
butO9 = Button(page1, text="O", font='arial 60', width=2, height=2)
butagain = Button(page1, text = "Рестарт", font='arial 20', width=6, height=1, command=again)
butexit = Button(page1, text = "Выход", font='arial 20', width=6, height=1, command=exit)

def main():
    page1.grid()
    but1.grid(row=1, column=1)
    but2.grid(row=1, column=2)
    but3.grid(row=1, column=3)
    but4.grid(row=2, column=1)
    but5.grid(row=2, column=2)
    but6.grid(row=2, column=3)
    but7.grid(row=3, column=1)
    but8.grid(row=3, column=2)
    but9.grid(row=3, column=3)
    butagain.grid(row=1, column=4)
    butexit.grid(row=2, column=4)
    root.mainloop()

main()