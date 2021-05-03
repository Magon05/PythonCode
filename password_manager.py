from tkinter import *
import random, sqlite3

global db
global sql

db = sqlite3.connect("server.db")#Подключаем базу данных
sql = db.cursor()#Подключаем объект для работы с базой данных
#Создаем родительский класс tkinter, окно его размеры и название
root = Tk()
root.title("Менеджер паролей")
root.resizable(False, False)
root.geometry('830x650')
#Словари по которым будет проводится шифровка и расшифровка данных
SYMBOLS = '1234567890qwertyuiopasdfghjklzxcvbnm@!?.,+;*/=:-_ASDFGHJKLZXCVBNMQWERTYUIOP '
SYMBOLS2 =" _ASDFGHJKLZXCVBNMQWERTYUIOPqwertyuiopasdfghjkl@!?.,+-*/=:;1234567890zxcvbnm"
#Создаем таблицу SQL если такой еще нет и подтверждаем действие
sql.execute("""CREATE TABLE IF NOT EXISTS list ( 
	site TEXT,
	login TEXT,
	password TEXT
	)""")
db.commit()

def main():#Основная функция запускающая программу

    def write():#Функция шифрует и записывает введенный текст в таблицу SQL
        adr = text1.get('1.0', END)
        log = text2.get('1.0', END)
        pas = text3.get('1.0', END)
        adrc = ""
        logc = ""
        pasc = ""
        for i in log:
            ind = SYMBOLS.find(i)
            logc += SYMBOLS2[ind]
        for i in pas:
            ind = SYMBOLS.find(i)
            pasc += SYMBOLS2[ind]
        for i in adr:
            ind = SYMBOLS.find(i)
            adrc += SYMBOLS2[ind]
        sql.execute(f"INSERT INTO list VALUES (?, ?, ?)", (adrc, logc, pasc))
        db.commit()

    def generate():#Функция генерирует пароли
        symbols = "asdfghjklqwertyuiopzxcvbnm1234567890!?-_ASDFGHJKLZXCVBNMQWERTYUIOP"
        password = ""
        while True:
            x = random.randrange(0, 66)
            i = symbols[x]
            if i in password:
                None
            elif len(password) == 12:
                break
            else:
                password += i
        text3.delete('1.0', END)
        text3.insert(1.0, password)

    def copy():#Функция копирует пароль в буфер обмена ПК
        finalpass = text3.get("1.0", END)
        root.clipboard_clear()
        root.clipboard_append(finalpass)

    def uncrypt():#Функция расшифровывает данные
        List = []
        for i in sql.execute("SELECT * FROM list"):
            text = ""
            uncryptadr = ""
            uncryptpas = ""
            uncryptlog = ""
            adr = i[0]
            log = i[1]
            pas = i[2]
            for i in pas:
                ind = SYMBOLS2.find(i)
                uncryptpas += SYMBOLS[ind]
            for i in log:
                ind = SYMBOLS2.find(i)
                uncryptlog += SYMBOLS[ind]
            for i in adr:
                ind = SYMBOLS2.find(i)
                uncryptadr += SYMBOLS[ind]
            text = uncryptadr + ">>>" + uncryptlog + ">>>" + uncryptpas
            List.append(text)
        window.delete("1.0", END)
        window.insert(1.0, List)

    #Создаем виджеты и размещаем их по местам в окне программы
    text1 = Text(root, height=2, width=20, font='Arial 14', wrap=WORD)
    text2 = Text(root, height=2, width=20, font='Arial 14', wrap=WORD)
    text3 = Text(root, height=2, width=20, font='Arial 14', wrap=WORD)
    label1 = Label(root, text="Введите адрес сайта", width=20, height=1, font='arial 15')
    label2 = Label(root, text="Введите логин", width=20, height=1, font='arial 15')
    label3 = Label(root, text="Введите пароль", width=20, height=1, font='arial 15')
    buttonwr = Button(root, height=2, width=15, font='Arial 14', text="Записать", command=write)
    buttongr = Button(root, height=2, width=15, font='Arial 14', text="Сгенирировать", command=generate)
    buttoncp = Button(root, height=2, width=15, font='Arial 14', text="Скопировать", command=copy)
    buttonsh = Button(root, height=2, width=15, font='Arial 14', text="Показать", command=uncrypt)
    window = Text(root, width="103", height="20")
    window.place(y=0, x=0)
    label1.place(y=400,x=0)
    text1.place(y=450,x=0)
    label2.place(y=400,x=300)
    text2.place(y=450,x=300)
    label3.place(y=400,x=600)
    text3.place(y=450,x=600)
    buttonwr.place(y=325,x=650)
    buttonsh.place(y=325,x=5)
    buttongr.place(y=505,x=625)
    buttoncp.place(y=575,x=625)

main()
root.mainloop()

