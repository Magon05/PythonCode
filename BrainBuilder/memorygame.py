from tkinter import *
import random

root = Tk()
root.title("Память")
pagemem = Frame(root)
words = ["собака", "кошка", "слон", "сова", "тигр", "лев", "пантера", "крокодил", "страус", "пингвин", "обезьяна", "тукан",
          "страус", "гепард", "буйвол", "мартышка", "бабуин", "змея", "кобра", "гадюка", "енот", "ежик", "мышь", "орел",
         "акула", "рысь", "слон", "бегемот", "питон", "бэтмен"]

def b1():
    def back():
        but1.grid(row=1, column=1)
        but2.grid(row=2, column=1)
        but3.grid(row=3, column=1)
        text1.grid_remove()
        text2.grid_remove()
        text3.grid_remove()
        text4.grid_remove()
        text5.grid_remove()
        butrem.grid_remove()
        butcheck.grid_remove()
        butback.grid_remove()

    def remember():
        text1.delete('1.0', END)
        text2.delete('1.0', END)
        text3.delete('1.0', END)
        text4.delete('1.0', END)
        text5.delete('1.0', END)

    def check():
        y1 = text1.get('1.0', END)
        y2 = text2.get('1.0', END)
        y3 = text3.get('1.0', END)
        y4 = text4.get('1.0', END)
        y5 = text5.get('1.0', END)
        if x1 == y1[:-1]:# метод text1.get вставляет в конце слова пробел, поэтому приходится делать так
            text1.delete('1.0', END)
            text1.insert(1.0, "Правильно")
        else:
            text1.delete('1.0', END)
            text1.insert(1.0, "Ошибка")
        if x2 == y2[:-1]:
            text2.delete('1.0', END)
            text2.insert(1.0, "Правильно")
        else:
            text2.delete('1.0', END)
            text2.insert(1.0, "Ошибка")
        if x3 == y3[:-1]:
            text3.delete('1.0', END)
            text3.insert(1.0, "Правильно")
        else:
            text3.delete('1.0', END)
            text3.insert(1.0, "Ошибка")
        if x4 == y4[:-1]:
            text4.delete('1.0', END)
            text4.insert(1.0, "Правильно")
        else:
            text4.delete('1.0', END)
            text4.insert(1.0, "Ошибка")
        if x5 == y5[:-1]:
            text5.delete('1.0', END)
            text5.insert(1.0, "Правильно")
        else:
            text5.delete('1.0', END)
            text5.insert(1.0, "Ошибка")

    butrem = Button(pagemem, height=2, width=15, font='Arial 14', text="Очистить", command=remember)
    butcheck = Button(pagemem, height=2, width=15, font='Arial 14', text="Проверить", command=check)
    butback = Button(pagemem, height=2, width=15, font='Arial 14', text="Назад", command=back)

    but1.grid_remove()
    but2.grid_remove()
    but3.grid_remove()
    text1.grid(row=1, column=1)
    text2.grid(row=1, column=2)
    text3.grid(row=1, column=3)
    text4.grid(row=1, column=4)
    text5.grid(row=1, column=5)
    butrem.grid(row=2, column=1)
    butcheck.grid(row=2, column=5)
    butback.grid(row=2, column=3)

    x1 = random.choice(words)
    words.remove(x1)
    text1.insert(1.0, x1)

    x2 = random.choice(words)
    words.remove(x2)
    text2.insert(1.0, x2)

    x3 = random.choice(words)
    words.remove(x3)
    text3.insert(1.0, x3)

    x4 = random.choice(words)
    words.remove(x4)
    text4.insert(1.0, x4)

    x5 = random.choice(words)
    words.remove(x5)
    text5.insert(1.0, x5)

def b2():
    def back():
        but1.grid(row=1, column=1)
        but2.grid(row=2, column=1)
        but3.grid(row=3, column=1)
        text1.grid_remove()
        text2.grid_remove()
        text3.grid_remove()
        text4.grid_remove()
        text5.grid_remove()
        text6.grid_remove()
        text7.grid_remove()
        text8.grid_remove()
        text9.grid_remove()
        text10.grid_remove()
        butrem.grid_remove()
        butcheck.grid_remove()
        butback.grid_remove()

    def remember():
        text1.delete('1.0', END)
        text2.delete('1.0', END)
        text3.delete('1.0', END)
        text4.delete('1.0', END)
        text5.delete('1.0', END)
        text6.delete('1.0', END)
        text7.delete('1.0', END)
        text8.delete('1.0', END)
        text9.delete('1.0', END)
        text10.delete('1.0', END)

    def check():
        y1 = text1.get('1.0', END)
        y2 = text2.get('1.0', END)
        y3 = text3.get('1.0', END)
        y4 = text4.get('1.0', END)
        y5 = text5.get('1.0', END)
        y6 = text6.get('1.0', END)
        y7 = text7.get('1.0', END)
        y8 = text8.get('1.0', END)
        y9 = text9.get('1.0', END)
        y10 = text10.get('1.0', END)
        if x1 == y1[:-1]:# метод text1.get вставляет в конце слова пробел, поэтому приходится делать так
            text1.delete('1.0', END)
            text1.insert(1.0, "Правильно")
        else:
            text1.delete('1.0', END)
            text1.insert(1.0, "Ошибка")
        if x2 == y2[:-1]:
            text2.delete('1.0', END)
            text2.insert(1.0, "Правильно")
        else:
            text2.delete('1.0', END)
            text2.insert(1.0, "Ошибка")
        if x3 == y3[:-1]:
            text3.delete('1.0', END)
            text3.insert(1.0, "Правильно")
        else:
            text3.delete('1.0', END)
            text3.insert(1.0, "Ошибка")
        if x4 == y4[:-1]:
            text4.delete('1.0', END)
            text4.insert(1.0, "Правильно")
        else:
            text4.delete('1.0', END)
            text4.insert(1.0, "Ошибка")
        if x5 == y5[:-1]:
            text5.delete('1.0', END)
            text5.insert(1.0, "Правильно")
        else:
            text5.delete('1.0', END)
            text5.insert(1.0, "Ошибка")
        if x6 == y6[:-1]:
            text6.delete('1.0', END)
            text6.insert(1.0, "Правильно")
        else:
            text6.delete('1.0', END)
            text6.insert(1.0, "Ошибка")
        if x7 == y7[:-1]:
            text7.delete('1.0', END)
            text7.insert(1.0, "Правильно")
        else:
            text7.delete('1.0', END)
            text7.insert(1.0, "Ошибка")
        if x8 == y8[:-1]:
            text8.delete('1.0', END)
            text8.insert(1.0, "Правильно")
        else:
            text8.delete('1.0', END)
            text8.insert(1.0, "Ошибка")
        if x9 == y9[:-1]:
            text9.delete('1.0', END)
            text9.insert(1.0, "Правильно")
        else:
            text9.delete('1.0', END)
            text9.insert(1.0, "Ошибка")
        if x10 == y10[:-1]:
            text10.delete('1.0', END)
            text10.insert(1.0, "Правильно")
        else:
            text10.delete('1.0', END)
            text10.insert(1.0, "Ошибка")

    butrem = Button(pagemem, height=2, width=15, font='Arial 14', text="Очистить", command=remember)
    butcheck = Button(pagemem, height=2, width=15, font='Arial 14', text="Проверить", command=check)
    butback = Button(pagemem, height=2, width=15, font='Arial 14', text="Назад", command=back)

    but1.grid_remove()
    but2.grid_remove()
    but3.grid_remove()
    text1.grid(row=1, column=1)
    text2.grid(row=1, column=2)
    text3.grid(row=1, column=3)
    text4.grid(row=1, column=4)
    text5.grid(row=1, column=5)
    text6.grid(row=2, column=1)
    text7.grid(row=2, column=2)
    text8.grid(row=2, column=3)
    text9.grid(row=2, column=4)
    text10.grid(row=2, column=5)
    butrem.grid(row=3, column=1)
    butcheck.grid(row=3, column=5)
    butback.grid(row=3, column=3)

    x1 = random.choice(words)
    words.remove(x1)
    text1.insert(1.0, x1)

    x2 = random.choice(words)
    words.remove(x2)
    text2.insert(1.0, x2)

    x3 = random.choice(words)
    words.remove(x3)
    text3.insert(1.0, x3)

    x4 = random.choice(words)
    words.remove(x4)
    text4.insert(1.0, x4)

    x5 = random.choice(words)
    words.remove(x5)
    text5.insert(1.0, x5)

    x6 = random.choice(words)
    words.remove(x6)
    text6.insert(1.0, x6)

    x7 = random.choice(words)
    words.remove(x7)
    text7.insert(1.0, x7)

    x8 = random.choice(words)
    words.remove(x8)
    text8.insert(1.0, x8)

    x9 = random.choice(words)
    words.remove(x9)
    text9.insert(1.0, x9)

    x10 = random.choice(words)
    words.remove(x10)
    text10.insert(1.0, x10)

def b3():
    def back():
        but1.grid(row=1, column=1)
        but2.grid(row=2, column=1)
        but3.grid(row=3, column=1)
        text1.grid_remove()
        text2.grid_remove()
        text3.grid_remove()
        text4.grid_remove()
        text5.grid_remove()
        text6.grid_remove()
        text7.grid_remove()
        text8.grid_remove()
        text9.grid_remove()
        text10.grid_remove()
        text11.grid_remove()
        text12.grid_remove()
        text13.grid_remove()
        text14.grid_remove()
        text15.grid_remove()
        butrem.grid_remove()
        butcheck.grid_remove()
        butback.grid_remove()

    def remember():
        text1.delete('1.0', END)
        text2.delete('1.0', END)
        text3.delete('1.0', END)
        text4.delete('1.0', END)
        text5.delete('1.0', END)
        text6.delete('1.0', END)
        text7.delete('1.0', END)
        text8.delete('1.0', END)
        text9.delete('1.0', END)
        text10.delete('1.0', END)
        text11.delete('1.0', END)
        text12.delete('1.0', END)
        text13.delete('1.0', END)
        text14.delete('1.0', END)
        text15.delete('1.0', END)

    def check():
        y1 = text1.get('1.0', END)
        y2 = text2.get('1.0', END)
        y3 = text3.get('1.0', END)
        y4 = text4.get('1.0', END)
        y5 = text5.get('1.0', END)
        y6 = text6.get('1.0', END)
        y7 = text7.get('1.0', END)
        y8 = text8.get('1.0', END)
        y9 = text9.get('1.0', END)
        y10 = text10.get('1.0', END)
        y11 = text11.get('1.0', END)
        y12 = text12.get('1.0', END)
        y13 = text13.get('1.0', END)
        y14 = text14.get('1.0', END)
        y15 = text15.get('1.0', END)
        if x1 == y1[:-1]:# метод text1.get вставляет в конце слова пробел, поэтому приходится делать так
            text1.delete('1.0', END)
            text1.insert(1.0, "Правильно")
        else:
            text1.delete('1.0', END)
            text1.insert(1.0, "Ошибка")
        if x2 == y2[:-1]:
            text2.delete('1.0', END)
            text2.insert(1.0, "Правильно")
        else:
            text2.delete('1.0', END)
            text2.insert(1.0, "Ошибка")
        if x3 == y3[:-1]:
            text3.delete('1.0', END)
            text3.insert(1.0, "Правильно")
        else:
            text3.delete('1.0', END)
            text3.insert(1.0, "Ошибка")
        if x4 == y4[:-1]:
            text4.delete('1.0', END)
            text4.insert(1.0, "Правильно")
        else:
            text4.delete('1.0', END)
            text4.insert(1.0, "Ошибка")
        if x5 == y5[:-1]:
            text5.delete('1.0', END)
            text5.insert(1.0, "Правильно")
        else:
            text5.delete('1.0', END)
            text5.insert(1.0, "Ошибка")
        if x6 == y6[:-1]:
            text6.delete('1.0', END)
            text6.insert(1.0, "Правильно")
        else:
            text6.delete('1.0', END)
            text6.insert(1.0, "Ошибка")
        if x7 == y7[:-1]:
            text7.delete('1.0', END)
            text7.insert(1.0, "Правильно")
        else:
            text7.delete('1.0', END)
            text7.insert(1.0, "Ошибка")
        if x8 == y8[:-1]:
            text8.delete('1.0', END)
            text8.insert(1.0, "Правильно")
        else:
            text8.delete('1.0', END)
            text8.insert(1.0, "Ошибка")
        if x9 == y9[:-1]:
            text9.delete('1.0', END)
            text9.insert(1.0, "Правильно")
        else:
            text9.delete('1.0', END)
            text9.insert(1.0, "Ошибка")
        if x10 == y10[:-1]:
            text10.delete('1.0', END)
            text10.insert(1.0, "Правильно")
        else:
            text10.delete('1.0', END)
            text10.insert(1.0, "Ошибка")
        if x11 == y11[:-1]:
            text11.delete('1.0', END)
            text11.insert(1.0, "Правильно")
        else:
            text11.delete('1.0', END)
            text11.insert(1.0, "Ошибка")
        if x12 == y12[:-1]:
            text12.delete('1.0', END)
            text12.insert(1.0, "Правильно")
        else:
            text12.delete('1.0', END)
            text12.insert(1.0, "Ошибка")
        if x13 == y13[:-1]:
            text13.delete('1.0', END)
            text13.insert(1.0, "Правильно")
        else:
            text13.delete('1.0', END)
            text13.insert(1.0, "Ошибка")
        if x14 == y14[:-1]:
            text14.delete('1.0', END)
            text14.insert(1.0, "Правильно")
        else:
            text14.delete('1.0', END)
            text14.insert(1.0, "Ошибка")
        if x15 == y15[:-1]:
            text15.delete('1.0', END)
            text15.insert(1.0, "Правильно")
        else:
            text15.delete('1.0', END)
            text15.insert(1.0, "Ошибка")

    butrem = Button(pagemem, height=2, width=15, font='Arial 14', text="Очистить", command=remember)
    butcheck = Button(pagemem, height=2, width=15, font='Arial 14', text="Проверить", command=check)
    butback = Button(pagemem, height=2, width=15, font='Arial 14', text="Назад", command=back)

    but1.grid_remove()
    but2.grid_remove()
    but3.grid_remove()
    text1.grid(row=1, column=1)
    text2.grid(row=1, column=2)
    text3.grid(row=1, column=3)
    text4.grid(row=1, column=4)
    text5.grid(row=1, column=5)
    text6.grid(row=2, column=1)
    text7.grid(row=2, column=2)
    text8.grid(row=2, column=3)
    text9.grid(row=2, column=4)
    text10.grid(row=2, column=5)
    text11.grid(row=3, column=1)
    text12.grid(row=3, column=2)
    text13.grid(row=3, column=3)
    text14.grid(row=3, column=4)
    text15.grid(row=3, column=5)
    butrem.grid(row=4, column=1)
    butcheck.grid(row=4, column=5)
    butback.grid(row=4, column=3)

    x1 = random.choice(words)
    words.remove(x1)
    text1.insert(1.0, x1)

    x2 = random.choice(words)
    words.remove(x2)
    text2.insert(1.0, x2)

    x3 = random.choice(words)
    words.remove(x3)
    text3.insert(1.0, x3)

    x4 = random.choice(words)
    words.remove(x4)
    text4.insert(1.0, x4)

    x5 = random.choice(words)
    words.remove(x5)
    text5.insert(1.0, x5)

    x6 = random.choice(words)
    words.remove(x6)
    text6.insert(1.0, x6)

    x7 = random.choice(words)
    words.remove(x7)
    text7.insert(1.0, x7)

    x8 = random.choice(words)
    words.remove(x8)
    text8.insert(1.0, x8)

    x9 = random.choice(words)
    words.remove(x9)
    text9.insert(1.0, x9)

    x10 = random.choice(words)
    words.remove(x10)
    text10.insert(1.0, x10)

    x11 = random.choice(words)
    words.remove(x11)
    text11.insert(1.0, x11)

    x12 = random.choice(words)
    words.remove(x12)
    text12.insert(1.0, x12)

    x13 = random.choice(words)
    words.remove(x13)
    text13.insert(1.0, x13)

    x14 = random.choice(words)
    words.remove(x14)
    text14.insert(1.0, x14)

    x15 = random.choice(words)
    words.remove(x15)
    text15.insert(1.0, x15)

but1 = Button(pagemem,height=2,width=15,font='Arial 14',text="Легко",command=b1)
but2 = Button(pagemem,height=2,width=15,font='Arial 14',text="Средне",command=b2)
but3 = Button(pagemem,height=2,width=15,font='Arial 14',text="Тяжело",command=b3)
text1 = Text(pagemem,height=1,width=10,font='Arial 32')
text2 = Text(pagemem,height=1,width=10,font='Arial 32')
text3 = Text(pagemem,height=1,width=10,font='Arial 32')
text4 = Text(pagemem,height=1,width=10,font='Arial 32')
text5 = Text(pagemem,height=1,width=10,font='Arial 32')
text6 = Text(pagemem,height=1,width=10,font='Arial 32')
text7 = Text(pagemem,height=1,width=10,font='Arial 32')
text8 = Text(pagemem,height=1,width=10,font='Arial 32')
text9 = Text(pagemem,height=1,width=10,font='Arial 32')
text10 = Text(pagemem,height=1,width=10,font='Arial 32')
text11 = Text(pagemem,height=1,width=10,font='Arial 32')
text12 = Text(pagemem,height=1,width=10,font='Arial 32')
text13 = Text(pagemem,height=1,width=10,font='Arial 32')
text14 = Text(pagemem,height=1,width=10,font='Arial 32')
text15 = Text(pagemem,height=1,width=10,font='Arial 32')

def run():
    pagemem.grid()
    but1.grid(row=1,column=1)
    but2.grid(row=2,column=1)
    but3.grid(row=3,column=1)
    root.mainloop()