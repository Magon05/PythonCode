from tkinter import *
import os

root = Tk()
root.title("Блокнот")
root.resizable(False, False)
root.geometry('830x550')

stroki = 1
zapros = ""

def main():

    def search():
        global zapros, stroki
        zapros = text1.get("1.0", END)
        text1.delete('1.0', END)
        text3.delete('1.0', END)
        file_types = ".txt"
        files = os.listdir('.')
        txtfiles = [f for f in files if f.split('.')[-1] in file_types]
        findedfile = []
        for f in txtfiles:
            with open(f) as txt:
                text = txt.read().splitlines()
                if zapros[0:-1] in text[0:stroki]:
                    findedfile.append(f)
        text3.insert(1.0, findedfile)

    def strings():
        global stroki
        stroki = int(text2.get("1.0", END))
        text2.delete('1.0', END)

    text1 = Text(root, width="103", height="2")
    text2 = Text(root, height=1, width=4, font='Arial 14', wrap=WORD)
    text3 = Text(root, width="103", height="2")
    label1 = Label(root, text="Текст запроса для поиска", width=50, height=1, font='arial 15')
    label2 = Label(root, text="Количество сканируемых строк(начиная с первой)", width=50, height=1, font='arial 15')
    label3 = Label(root, text="Результат:", width=50, height=1, font='arial 15')
    buttonsearch = Button(root, height=2, width=15, font='Arial 14', text="Поиск", command=search)
    buttonstrings = Button(root, height=2, width=15, font='Arial 14', text="Задать", command=strings)

    label1.place(y=50, x=130)
    text1.place(y=100, x=0)
    buttonsearch.place(y=150, x=325)
    label2.place(y=250, x=130)
    text2.place(y=300,x=390)
    buttonstrings.place(y=350,x=325)
    label3.place(y=450, x=130)
    text3.place(y=500, x=0)

main()
root.mainloop()