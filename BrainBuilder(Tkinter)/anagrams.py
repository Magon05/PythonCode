from tkinter import *
import random

root = Tk()
root.title("Анаграммы")
pagean = Frame(root)
words = ["собака", "кошка", "слон", "сова", "тигр", "лев", "пантера", "крокодил", "страус", "пингвин", "обезьяна", "тукан",
          "страус", "гепард", "буйвол", "мартышка", "бабуин", "змея", "кобра", "гадюка", "енот", "ежик", "мышь", "орел",
         "акула", "рысь", "слон", "бегемот", "питон", "бэтмен"]
wordanswer = ""
word1 = ""
word2 = ""
word3 = ""
word4 = ""

def generate():
    global wordanswer,word1,word2,word3,word4
    word = []

    word1 = random.choice(words)
    words.remove(word1)
    word.append(word1)

    word2 = random.choice(words)
    words.remove(word2)
    word.append(word2)

    word3 = random.choice(words)
    words.remove(word3)
    word.append(word3)

    word4 = random.choice(words)
    words.remove(word4)
    word.append(word4)

    wordanswer = random.choice(word)
    word_sorted1 = "".join(sorted(word1))
    word_sorted2 = "".join(sorted(word2))
    word_sorted3 = "".join(sorted(word3))
    word_sorted4 = "".join(sorted(word4))
    text1.delete('1.0', END)
    text2.delete('1.0', END)
    text3.delete('1.0', END)
    text4.delete('1.0', END)
    text1.insert(1.0, word_sorted1)
    text2.insert(1.0, word_sorted2)
    text3.insert(1.0, word_sorted3)
    text4.insert(1.0, word_sorted4)

    label = Label(pagean, text=wordanswer, width=20, height=1, font='arial 32')
    label.grid_remove()
    label.grid(row=1, column=2)

def b1():
    if word1 == wordanswer:
        text1.delete('1.0', END)
        text1.insert(1.0, "Верно")
    else:
        text1.delete('1.0', END)
        text1.insert(1.0, "Ошибка")

def b2():
    if word2 == wordanswer:
        text2.delete('1.0', END)
        text2.insert(1.0, "Верно")
    else:
        text2.delete('1.0', END)
        text2.insert(1.0, "Ошибка")

def b3():
    if word3 == wordanswer:
        text3.delete('1.0', END)
        text3.insert(1.0, "Верно")
    else:
        text3.delete('1.0', END)
        text3.insert(1.0, "Ошибка")

def b4():
    if word4 == wordanswer:
        text4.delete('1.0', END)
        text4.insert(1.0, "Верно")
    else:
        text4.delete('1.0', END)
        text4.insert(1.0, "Ошибка")

text1 = Text(pagean,height=1,width=10,font='Arial 32')
text2 = Text(pagean,height=1,width=10,font='Arial 32')
text3 = Text(pagean,height=1,width=10,font='Arial 32')
text4 = Text(pagean,height=1,width=10,font='Arial 32')
but1 = Button(pagean,height=2,width=15,font='Arial 14',text="Ответ", command=b1)
but2 = Button(pagean,height=2,width=15,font='Arial 14',text="Ответ", command=b2)
but3 = Button(pagean,height=2,width=15,font='Arial 14',text="Ответ", command=b3)
but4 = Button(pagean,height=2,width=15,font='Arial 14',text="Ответ", command=b4)
butgenerate = Button(pagean,height=2,width=15,font='Arial 14',text="Сгенерировать", command=generate)

def run():
    pagean.grid()
    text1.grid(row=2,column=1)
    but1.grid(row=3,column=1)
    text2.grid(row=2,column=3)
    but2.grid(row=3,column=3)
    text3.grid(row=4,column=1)
    but3.grid(row=5,column=1)
    text4.grid(row=4,column=3)
    but4.grid(row=5,column=3)
    butgenerate.grid(row=3,column=2)
    root.mainloop()