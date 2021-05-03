#Данная программа является каталогизатором фильмов и не только, можно адаптировать и под музыку и книги.Удобство в том что не нужно пользоваться проводником, а можно запустить программу с рабочего стола. 
#Вы указываете где находится запускаемый файл и изображение для виджета которое вы хотите.
import tkinter, os, subprocess
from PIL import Image, ImageTk

#Создаем родительский класс tkinter
root = tkinter.Tk()
root.title("Фильмы")

# создаем страницы
page1 = tkinter.Frame(root)
page2 = tkinter.Frame(root)

#Функции кнопок следующая и предыдущая страница
def next_page(self):
    page2.grid()
    page1.grid_remove()

def back_page(self):
    page2.grid_remove()
    page1.grid()

#Функции запуска фильмов
def b1(self):
    os.startfile("F:\Фильмы\Гладиатор\Gladiator.mkv")

def b2(self):
    os.startfile("F:\Фильмы\Властелин колец\Властелин колец - Братство кольца\Властелин колец - Братство кольца.mkv")

def b3(self):
    os.startfile("F:\Фильмы\Властелин колец\The Lord of the Rings The Two Towers\The.Lord.of.the.Rings.The.Two.Towers.mp4")

def b4(self):
    os.startfile("F:\Фильмы\Властелин колец\The Lord of the Rings The Return of the King\The.Lord.of.the.Rings.The.Return.of.the.King.mp4")

def b5(self):
    os.startfile("F:\Фильмы\Блэйд\БЛЭЙД.mkv")

def b6(self):
    os.startfile("F:\Фильмы\Блэйд\Blade.II.mkv")

def b7(self):
    os.startfile("F:\Фильмы\Блэйд\БЛЭЙД-3 (Троица).mkv")

def b8(self):
    os.startfile("F:\Фильмы\Александр.mkv")

def b9(self):
    os.startfile("F:\Фильмы\Центурион.mkv")

def b10(self):
    os.startfile("F:\Фильмы\Скала.mkv")

def b11(self):
    os.startfile("F:\Фильмы\Храброе сердце.mkv")

def b12(self):
    os.startfile("F:\Фильмы\Поезд на Юму.mkv")

def b13(self):
    os.startfile("F:\Фильмы\Выживший.mkv")

def b14(self):
    os.startfile("F:\Фильмы\Недруги.mkv")

def b15(self):
    os.startfile("F:\Фильмы\The Gentlemen.mkv")

def b16(self):
    os.startfile("F:\Фильмы\Collector.mkv")

def b17(self):
    os.startfile("F:\Фильмы\Безумный Макс.mkv")

def b18(self):
    os.startfile("F:\Фильмы\Быстрее пули.mkv")

def b19(self):
    os.startfile("F:\Фильмы\Капитан Алатристе.mkv")

def b20(self):
    os.startfile("F:\Фильмы\Судья Дрэд.mkv")

def b21(self):
    os.startfile("F:\Фильмы\Робин Гуд.mkv")

def b22(self):
    os.startfile("F:\Фильмы\Нэд Келли.mkv")

def b23(self):
    os.startfile("F:\Фильмы\Омерзительная восьмерка.mkv")

def b24(self):
    os.startfile("F:\Фильмы\Последний самурай.mkv")

def b25(self):
    os.startfile("F:\Фильмы\Ярость.mkv")

def b26(self):
    os.startfile("F:\Фильмы\Троя.mkv")

def b27(self):
    os.startfile("F:\Фильмы\Жизнь ПИ.mkv")

def b28(self):
    os.startfile("F:\Фильмы\Джонни Д.mkv")

def b29(self):
    os.startfile("F:\Фильмы\Планета обезьян\Планета обезьян.mkv")

def b30(self):
    os.startfile("F:\Фильмы\Планета обезьян\Планета обезьян 3.mkv")

def b31(self):
    os.startfile("F:\Фильмы\Хроники Риддика\Хроники Риддика.mkv")

def b32(self):
    os.startfile("F:\Фильмы\Хроники Риддика\Хронники Риддика 2.mkv")

def b33(self):
    os.startfile("F:\Фильмы\Бетмэн\Batman Begins\Batman.Begins.mp4")

def b34(self):
    os.startfile("F:\Фильмы\Бетмэн\The Dark Knight.mkv")

def b35(self):
    os.startfile("F:\Фильмы\Бетмэн\The Dark Knight Rises\The.Dark.Knight.Rises.mp4")

def b36(self):
    os.startfile("F:\Фильмы\\127 часов.mkv")

def b37(self):
    os.startfile("F:\Фильмы\\13й воин.mkv")

def b38(self):
    os.startfile("F:\Фильмы\Бойцовский клуб.mkv")

def b39(self):
    os.startfile("F:\Фильмы\Враг у ворот.mkv")

def b40(self):
    os.startfile("F:\Фильмы\Жанна Дарк.mkv")

def b41(self):
    os.startfile("F:\Фильмы\\5й элемент.mkv")

def b42(self):
    os.startfile("F:\Фильмы\\13.mkv")

# Алгоритм загрузки изображения: сначала загружаем его указывая адрес затем преобразуем в нужный для tkinter формат
imagenp = Image.open("D:\Изображения\Кино\\np.jpg")
photonp = ImageTk.PhotoImage(imagenp)

imagebp = Image.open("D:\Изображения\Кино\\bp.jpg")
photobp = ImageTk.PhotoImage(imagebp)

image1 = Image.open("D:\Изображения\Кино\gla.jpg")
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open("D:\Изображения\Кино\lor1.jpg")
photo2 = ImageTk.PhotoImage(image2)

image3 = Image.open("D:\Изображения\Кино\lor2.jpg")
photo3 = ImageTk.PhotoImage(image3)

image4 = Image.open("D:\Изображения\Кино\lor3.jpg")
photo4 = ImageTk.PhotoImage(image4)

image5 = Image.open("D:\Изображения\Кино\\bla1.jpg")
photo5 = ImageTk.PhotoImage(image5)

image6 = Image.open("D:\Изображения\Кино\\bla2.jpg")
photo6 = ImageTk.PhotoImage(image6)

image7 = Image.open("D:\Изображения\Кино\\bla3.jpg")
photo7 = ImageTk.PhotoImage(image7)

image8 = Image.open("D:\Изображения\Кино\\alx.jpg")
photo8 = ImageTk.PhotoImage(image8)

image9 = Image.open("D:\Изображения\Кино\cen.jpg")
photo9 = ImageTk.PhotoImage(image9)

image10 = Image.open("D:\Изображения\Кино\\roc.jpg")
photo10 = ImageTk.PhotoImage(image10)

image11 = Image.open("D:\Изображения\Кино\\bra.jpg")
photo11 = ImageTk.PhotoImage(image11)

image12 = Image.open("D:\Изображения\Кино\\uma.jpg")
photo12 = ImageTk.PhotoImage(image12)

image13 = Image.open("D:\Изображения\Кино\\ali.jpg")
photo13 = ImageTk.PhotoImage(image13)

image14 = Image.open("D:\Изображения\Кино\hat.jpg")
photo14 = ImageTk.PhotoImage(image14)

image15 = Image.open("D:\Изображения\Кино\jen.jpg")
photo15 = ImageTk.PhotoImage(image15)

image16 = Image.open("D:\Изображения\Кино\col.jpg")
photo16 = ImageTk.PhotoImage(image16)

image17 = Image.open("D:\Изображения\Кино\max.jpg")
photo17 = ImageTk.PhotoImage(image17)

image18 = Image.open("D:\Изображения\Кино\\fas.jpg")
photo18 = ImageTk.PhotoImage(image18)

image19 = Image.open("D:\Изображения\Кино\\alt.jpg")
photo19 = ImageTk.PhotoImage(image19)

image20 = Image.open("D:\Изображения\Кино\dre.jpg")
photo20 = ImageTk.PhotoImage(image20)

image21 = Image.open("D:\Изображения\Кино\\rob.jpg")
photo21 = ImageTk.PhotoImage(image21)

image22 = Image.open("D:\Изображения\Кино\\ned.jpg")
photo22 = ImageTk.PhotoImage(image22)

image23 = Image.open("D:\Изображения\Кино\\8.jpg")
photo23 = ImageTk.PhotoImage(image23)

image24 = Image.open("D:\Изображения\Кино\\sam.jpg")
photo24 = ImageTk.PhotoImage(image24)

image25 = Image.open("D:\Изображения\Кино\\fury.jpg")
photo25 = ImageTk.PhotoImage(image25)

image26 = Image.open("D:\Изображения\Кино\\troy.jpg")
photo26 = ImageTk.PhotoImage(image26)

image27 = Image.open("D:\Изображения\Кино\\pi.jpg")
photo27 = ImageTk.PhotoImage(image27)

image28 = Image.open("D:\Изображения\Кино\\D.jpg")
photo28 = ImageTk.PhotoImage(image28)

image29 = Image.open("D:\Изображения\Кино\\abe1.jpg")
photo29 = ImageTk.PhotoImage(image29)

image30 = Image.open("D:\Изображения\Кино\\abe2.jpg")
photo30 = ImageTk.PhotoImage(image30)

image31 = Image.open("D:\Изображения\Кино\\rid1.jpg")
photo31 = ImageTk.PhotoImage(image31)

image32 = Image.open("D:\Изображения\Кино\\rid2.jpg")
photo32 = ImageTk.PhotoImage(image32)

image33 = Image.open("D:\Изображения\Кино\\bat1.jpg")
photo33 = ImageTk.PhotoImage(image33)

image34 = Image.open("D:\Изображения\Кино\\bat2.jpg")
photo34 = ImageTk.PhotoImage(image34)

image35 = Image.open("D:\Изображения\Кино\\bat3.jpg")
photo35 = ImageTk.PhotoImage(image35)

image36 = Image.open("D:\Изображения\Кино\\127.jpg")
photo36 = ImageTk.PhotoImage(image36)

image37 = Image.open("D:\Изображения\Кино\\13w.jpg")
photo37 = ImageTk.PhotoImage(image37)

image38 = Image.open("D:\Изображения\Кино\\fc.jpg")
photo38 = ImageTk.PhotoImage(image38)

image39 = Image.open("D:\Изображения\Кино\\eag.jpg")
photo39 = ImageTk.PhotoImage(image39)

image40 = Image.open("D:\Изображения\Кино\\jd.jpg")
photo40 = ImageTk.PhotoImage(image40)

image41 = Image.open("D:\Изображения\Кино\\5.jpg")
photo41 = ImageTk.PhotoImage(image41)

image42 = Image.open("D:\Изображения\Кино\\13.jpg")
photo42 = ImageTk.PhotoImage(image42)


# создаем кнопки привязываем их к нужной странице и ставим изображения
butnp = tkinter.Button(page1, image = photonp, width=100,height=100)
butnp.bind('<Button-1>', next_page)

butbp = tkinter.Button(page2, image = photobp, width=100,height=100)
butbp.bind('<Button-1>', back_page)

but1 = tkinter.Button(page1, image=photo1, width=240,height=320)
but1.bind('<Button-1>', b1)

but2 = tkinter.Button(page1, image=photo2, width=240,height=320)
but2.bind('<Button-1>', b2)

but3 = tkinter.Button(page1, image=photo3, width=240,height=320)
but3.bind('<Button-1>', b3)

but4 = tkinter.Button(page1, image=photo4, width=240,height=320)
but4.bind('<Button-1>', b4)

but5 = tkinter.Button(page1, image=photo5, width=240,height=320)
but5.bind('<Button-1>', b5)

but6 = tkinter.Button(page1, image=photo6, width=240,height=320)
but6.bind('<Button-1>', b6)

but7 = tkinter.Button(page1, image=photo7, width=240,height=320)
but7.bind('<Button-1>', b7)

but8 = tkinter.Button(page1, image=photo8, width=240,height=320)
but8.bind('<Button-1>', b8)

but9 = tkinter.Button(page1, image=photo9, width=240,height=320)
but9.bind('<Button-1>', b9)

but10 = tkinter.Button(page1, image=photo10, width=240,height=320)
but10.bind('<Button-1>', b10)

but11 = tkinter.Button(page1, image=photo11, width=240,height=320)
but11.bind('<Button-1>', b11)

but12 = tkinter.Button(page1, image=photo12, width=240,height=320)
but12.bind('<Button-1>', b12)

but13 = tkinter.Button(page1, image=photo13, width=240,height=320)
but13.bind('<Button-1>', b13)

but14 = tkinter.Button(page1, image=photo14, width=240,height=320)
but14.bind('<Button-1>', b14)

but15 = tkinter.Button(page1, image=photo15, width=240,height=320)
but15.bind('<Button-1>', b15)

but16 = tkinter.Button(page1, image=photo16, width=240,height=320)
but16.bind('<Button-1>', b16)

but17 = tkinter.Button(page1, image=photo17, width=240,height=320)
but17.bind('<Button-1>', b17)

but18 = tkinter.Button(page1, image=photo18, width=240,height=320)
but18.bind('<Button-1>', b18)

but19 = tkinter.Button(page1, image=photo19, width=240,height=320)
but19.bind('<Button-1>', b19)

but20 = tkinter.Button(page1, image=photo20, width=240,height=320)
but20.bind('<Button-1>', b20)

but21 = tkinter.Button(page1, image=photo21, width=240,height=320)
but21.bind('<Button-1>', b21)

but22 = tkinter.Button(page2, image=photo22, width=240,height=320)
but22.bind('<Button-1>', b22)

but23 = tkinter.Button(page2, image=photo23, width=240,height=320)
but23.bind('<Button-1>', b23)

but24 = tkinter.Button(page2, image=photo24, width=240,height=320)
but24.bind('<Button-1>', b24)

but25 = tkinter.Button(page2, image=photo25, width=240,height=320)
but25.bind('<Button-1>', b25)

but26 = tkinter.Button(page2, image=photo26, width=240,height=320)
but26.bind('<Button-1>', b26)

but27 = tkinter.Button(page2, image=photo27, width=240,height=320)
but27.bind('<Button-1>', b27)

but28 = tkinter.Button(page2, image=photo28, width=240,height=320)
but28.bind('<Button-1>', b28)

but29 = tkinter.Button(page2, image=photo29, width=240,height=320)
but29.bind('<Button-1>', b29)

but30 = tkinter.Button(page2, image=photo30, width=240,height=320)
but30.bind('<Button-1>', b30)

but31 = tkinter.Button(page2, image=photo31, width=240,height=320)
but31.bind('<Button-1>', b31)

but32 = tkinter.Button(page2, image=photo32, width=240,height=320)
but32.bind('<Button-1>', b32)

but33 = tkinter.Button(page2, image=photo33, width=240,height=320)
but33.bind('<Button-1>', b33)

but34 = tkinter.Button(page2, image=photo34, width=240,height=320)
but34.bind('<Button-1>', b34)

but35 = tkinter.Button(page2, image=photo35, width=240,height=320)
but35.bind('<Button-1>', b35)

but36 = tkinter.Button(page2, image=photo36, width=240,height=320)
but36.bind('<Button-1>', b36)

but37 = tkinter.Button(page2, image=photo37, width=240,height=320)
but37.bind('<Button-1>', b37)

but38 = tkinter.Button(page2, image=photo38, width=240,height=320)
but38.bind('<Button-1>', b38)

but39 = tkinter.Button(page2, image=photo39, width=240,height=320)
but39.bind('<Button-1>', b39)

but40 = tkinter.Button(page2, image=photo40, width=240,height=320)
but40.bind('<Button-1>', b40)

but41 = tkinter.Button(page2, image=photo41, width=240,height=320)
but41.bind('<Button-1>', b41)

but42 = tkinter.Button(page2, image=photo42, width=240,height=320)
but42.bind('<Button-1>', b42)

#Ставим элементы на позиции в окне
page1.grid()
butnp.grid(row=3, column=8)
butbp.grid(row=1, column=8)
but1.grid(row=1, column=1)
but2.grid(row=1, column=2)
but3.grid(row=1, column=3)
but4.grid(row=1, column=4)
but5.grid(row=1, column=5)
but6.grid(row=1, column=6)
but7.grid(row=1, column=7)
but8.grid(row=2, column=1)
but9.grid(row=2, column=2)
but10.grid(row=2, column=3)
but11.grid(row=2, column=4)
but12.grid(row=2, column=5)
but13.grid(row=2, column=6)
but14.grid(row=2, column=7)
but15.grid(row=3, column=1)
but16.grid(row=3, column=2)
but17.grid(row=3, column=3)
but18.grid(row=3, column=4)
but19.grid(row=3, column=5)
but20.grid(row=3, column=6)
but21.grid(row=3, column=7)
but22.grid(row=1, column=1)
but23.grid(row=1, column=2)
but24.grid(row=1, column=3)
but25.grid(row=1, column=4)
but26.grid(row=1, column=5)
but27.grid(row=1, column=6)
but28.grid(row=1, column=7)
but29.grid(row=2, column=1)
but30.grid(row=2, column=2)
but31.grid(row=2, column=3)
but32.grid(row=2, column=4)
but33.grid(row=2, column=5)
but34.grid(row=2, column=6)
but35.grid(row=2, column=7)
but36.grid(row=3, column=1)
but37.grid(row=3, column=2)
but38.grid(row=3, column=3)
but39.grid(row=3, column=4)
but40.grid(row=3, column=5)
but41.grid(row=3, column=6)
but42.grid(row=3, column=7)
root.mainloop()