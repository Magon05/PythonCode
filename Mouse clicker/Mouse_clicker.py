import pyautogui, time, keyboard


click = input("Сколько кликов нужно")
seconds = input("Сколько секунд между кликами?")
print("Наведи мышь на цель и жди...")
time.sleep(3)
print("Для выхода нажми и удерживай esc...")
print("5...")
time.sleep(1)
print("4...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")

for i in range(int(click)):
    if keyboard.is_pressed('esc'):
        print("Остановка...")
        break
    x, y = pyautogui.position()
    pyautogui.click(x, y)
    time.sleep(float(seconds))