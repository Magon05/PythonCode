import tkinter, mathgame, memorygame, anagrams

root = tkinter.Tk()
root.title("Главное меню")
pagemain = tkinter.Frame(root)

def b1():
    mathgame.run()

def b2():
    memorygame.run()

def b3():
    anagrams.run()

but1 = tkinter.Button(pagemain,height=2,width=15,font='Arial 14',text="Математика",command=b1,bg="yellow")
but2 = tkinter.Button(pagemain,height=2,width=15,font='Arial 14',text="Память",command=b2,bg="green")
but3 = tkinter.Button(pagemain,height=2,width=15,font='Arial 14',text="Анаграммы",command=b3,bg="red")

pagemain.grid()
but1.grid(row=1,column=1)
but2.grid(row=2, column=1)
but3.grid(row=3, column=1)
root.mainloop()