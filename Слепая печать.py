from tkinter import *
from PIL import Image, ImageTk
import random, time
from threading import Thread

lan = "rus"
sec = 0

def lanchange():
    global lan
    if lan == "rus":
        lan = "eng"
    else:
        lan = "rus"

def start():
    global sec
    eng = "qwertyuiopasdfghjklzxcvbnm"
    rus = "йцукенгшщзхъфывапролджэячсмитьбю"
    y = 0
    string = ""
    th = Thread(target=timer)
    th.start()
    text2.delete('1.0', END)
    text3.delete('1.0', END)
    text3.insert(1.0, sec)
    sec = 0
    if lan == "rus":
        while y < 45:
            y += 1
            x = random.randrange(0, 31)
            if len(string) == 9 or len(string) == 18 or len(string) == 27 or len(string) == 36 or len(string) == 45:
                string += " "
            string += rus[x]
            text1.delete('1.0', END)
            text1.insert(1.0, string)
    else:
        while y < 50:
            y += 1
            x = random.randrange(0, 26)
            if len(string) == 9 or len(string) == 18 or len(string) == 27 or len(string) == 36 or len(string) == 45:
                string += " "
            string += eng[x]
            text1.delete('1.0', END)
            text1.insert(1.0, string)

def timer():
    global sec
    while True:
        time.sleep(1)
        sec += 1

root = Tk()
page = Frame(root)
text1 = Text(page,height=1,width=50,font='Arial 32',wrap=WORD)
text2 = Text(page,height=1,width=50,font='Arial 32',wrap=WORD)
text3 = Text(page,height=1,width=6,font='Arial 32',wrap=WORD)
image = Image.open("image.png")
photo = ImageTk.PhotoImage(image)
but1 = Button(page, image=photo, width=1200,height=746)
but2 = Button(page,height=2,width=15,font='Arial 14',text="Rus/Eng",command=lanchange)
but3 = Button(page,height=2,width=15,font='Arial 14',text="Сгенерировать",command=start)

page.grid()
but1.grid(row=2, column=1)
but2.grid(row=1, column=2)
but3.grid(row=3, column=2)
text1.grid(row=1, column=1)
text2.grid(row=3, column=1)
text3.grid(row=2, column=2)
root.mainloop()