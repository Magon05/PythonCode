from tkinter import *
root = Tk()
text = Text(root,height=5,width=50,font='Arial 14',wrap=WORD)
button1 = Button(root,height=2,width=15,font='Arial 14',text="Зашифровать")
button2 = Button(root,height=2,width=15,font='Arial 14',text="Расшифровать")
button3 = Button(root,height=2,width=15,font='Arial 14',text="Копировать")
button4 = Button(root,height=2,width=15,font='Arial 14',text="Вставить")
SYMBOLS = '1234567890абвгдеежзийклмнопрстуфхцчшщъыьэюя !?.,+-*/=:; '
SYMBOLS2 = 'フブプヘペホポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ・ーヽヾヿビピ トドナニヌネノハバパヒ '

def crypt(self):
    encryptext = text.get('1.0', END)
    cryptext = ""
    for i in encryptext.lower():
        ind = SYMBOLS.find(i)
        cryptext += SYMBOLS2[ind]
    text.delete('1.0', END)
    text.insert(1.0, cryptext)

def encrypt(self):
    encryptext = ""
    cryptext = text.get('1.0', END)
    for i in cryptext:
        ind = SYMBOLS2.find(i)
        encryptext += SYMBOLS[ind]
    text.delete('1.0', END)
    text.insert(1.0, encryptext.capitalize())

def copy_button(self):
    textfinal = text.get("1.0", END)
    root.clipboard_clear()
    root.clipboard_append(textfinal)

def insert_button(self):
    textfinal = root.clipboard_get()
    root.clipboard_clear()
    text.insert("1.0", textfinal)

root.title("Шифровальщик сообщений")

button1.bind("<Button-1>", crypt)
button2.bind("<Button-1>", encrypt)
button3.bind("<Button-1>", copy_button)
button4.bind("<Button-1>", insert_button)
text.pack()
button1.pack(side="left")
button2.pack(side="right")
button3.pack(side="top")
button4.pack(side="top")
root.mainloop()