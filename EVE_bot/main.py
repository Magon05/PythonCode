import pyautogui, time

def main():# Данная функция проверяет наличие кнопки ускорения на экране, так мы узнаем в космосе мы или в доке. В зависимости есть ли кнопка или нет запускается определенная функция.
    locate = pyautogui.locateOnScreen('space.png')
    while True:
        time.sleep(60) # Таймер в 1 минуту перед совершением процедуры захода в док или выхода из него
        if locate == None:
            undocking()
        elif locate != None:
            docking()

def undocking():# Вы ходим из дока кликнув по кнопке мышкой
    pyautogui.click(x=1800, y=180, duration=1.0)

def docking():# Заходим в док выбрав на панели справа нужные разделы и нажав нужные кнопки
    pyautogui.click(x=1750, y=200, duration=1.0)
    time.sleep(1)
    pyautogui.moveTo(x=1750, y=310)
    time.sleep(1)
    pyautogui.scroll(-10000)
    time.sleep(1)
    pyautogui.keyDown("d")
    pyautogui.leftClick(x=1500, y=820, duration=1)
    pyautogui.leftClick(x=1500, y=820, duration=1)
    pyautogui.keyUp("d")

main()

