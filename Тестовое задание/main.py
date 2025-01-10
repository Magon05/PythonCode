import tkinter as tk
import psutil
import sqlite3
import time


# Создаем или подключаемся к базе данных SQLite
conn = sqlite3.connect('system_metrics.db')
c = conn.cursor()

# Создаем таблицу, если она не существует
c.execute('''
CREATE TABLE IF NOT EXISTS metrics (
    timestamp TEXT,
    cpu_usage REAL,
    ram_usage REAL,
    disk_usage REAL
)
''')
conn.commit()

# Глобальные переменные
recording = False
start_time = 0

def update_metrics():
    global recording, start_time

    # Получаем данные о загрузке ЦП, ОЗУ и ПЗУ
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    # Обновляем текстовые метрики в интерфейсе
    cpu_label.config(text=f"Загрузка ЦП: {cpu_usage}%")
    ram_label.config(text=f"Загрузка ОЗУ: {ram_usage}%")
    disk_label.config(text=f"Загрузка ПЗУ: {disk_usage}%")

    # Записываем данные в БД, если запись активна
    if recording:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        c.execute('INSERT INTO metrics (timestamp, cpu_usage, ram_usage, disk_usage) VALUES (?, ?, ?, ?)',
                  (timestamp, cpu_usage, ram_usage, disk_usage))
        conn.commit()

        # Обновляем таймер
        elapsed_time = time.time() - start_time
        timer_label.config(text=f"Время записи: {int(elapsed_time)} секунд")

    # Запланируем обновление через заданный интервал
    root.after(update_interval.get() * 1000, update_metrics)

def start_recording():
    global recording, start_time
    recording = True
    start_time = time.time()
    start_button.pack_forget()
    stop_button.pack()
    timer_label.pack()

def stop_recording():
    global recording, start_time
    start_time = 0
    recording = False
    stop_button.pack_forget()
    start_button.pack()
    timer_label.pack_forget()

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("История записей")

    # Получаем данные из БД
    c.execute('SELECT * FROM metrics')
    records = c.fetchall()

    for record in records:
        record_label = tk.Label(history_window, text=f"{record[0]} - ЦП: {record[1]}%, ОЗУ: {record[2]}%, ПЗУ: {record[3]}%")
        record_label.pack()

# Создаем главное окно приложения
root = tk.Tk()
root.title("Монитор ресурсов системы")

# Поле для задания интервала обновления
update_interval = tk.IntVar(value=1)
interval_entry = tk.Entry(root, textvariable=update_interval)
interval_entry.pack(pady=10)
interval_label = tk.Label(root, text="Введите интервал обновления (в секундах):")
interval_label.pack()

# Создаем метки для отображения информации
cpu_label = tk.Label(root, text="Загрузка ЦП: 0%", font=("Helvetica", 16))
cpu_label.pack(pady=10)

ram_label = tk.Label(root, text="Загрузка ОЗУ: 0%", font=("Helvetica", 16))
ram_label.pack(pady=10)

disk_label = tk.Label(root, text="Загрузка ПЗУ: 0%", font=("Helvetica", 16))
disk_label.pack(pady=10)

# Таймер
timer_label = tk.Label(root, text="", font=("Helvetica", 16))
timer_label.pack(pady=10)

# Кнопки для управления записью
start_button = tk.Button(root, text="Начать запись", command=start_recording)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Остановить", command=stop_recording)
stop_button.pack_forget()

history_button = tk.Button(root, text="Просмотреть историю", command=show_history)
history_button.pack(pady=10)

# Запускаем обновление метрик
update_metrics()

# Запускаем главный цикл приложения
root.mainloop()

# Закрываем соединение с БД при выходе
conn.close()