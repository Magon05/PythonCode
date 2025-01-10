import unittest
from unittest.mock import patch
import sqlite3
import os
from main import *


class TestSystemMonitor(unittest.TestCase):
    def setUp(self):
        # Создаем тестовую базу данных
        self.test_db = 'test_system_metrics.db'
        conn = sqlite3.connect(self.test_db)
        c = conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            timestamp TEXT,
            cpu_usage REAL,
            ram_usage REAL,
            disk_usage REAL
        )
        ''')
        conn.commit()
        conn.close()

    def tearDown(self):
        # Удаляем тестовую базу данных
        os.remove(self.test_db)

    @patch('psutil.cpu_percent')
    @patch('psutil.virtual_memory')
    @patch('psutil.disk_usage')
    def test_update_metrics(self, mock_disk_usage, mock_virtual_memory, mock_cpu_percent):
        # Настраиваем моки для тестирования
        mock_cpu_percent.return_value = 50.0
        mock_virtual_memory.return_value.percent = 60.0
        mock_disk_usage.return_value.percent = 70.0

        # Вызываем функцию update_metrics
        update_metrics()

        # Проверяем, что метрики были обновлены
        self.assertEqual(cpu_label.cget("text"), "Загрузка ЦП: 50.0%")
        self.assertEqual(ram_label.cget("text"), "Загрузка ОЗУ: 60.0%")
        self.assertEqual(disk_label.cget("text"), "Загрузка ПЗУ: 70.0%")

    def test_start_and_stop_recording(self):
        # Проверяем, что запись начинается и останавливается
        start_recording()
        self.assertTrue(recording)
        self.assertIsNotNone(start_time)
        self.assertIsNotNone(timer_label.cget("text"))

        stop_recording()
        self.assertFalse(recording)
        self.assertIsNone(timer_label.cget("text"))

    def test_show_history(self):
        # Записываем данные в тестовую базу данных
        c.execute('INSERT INTO metrics (timestamp, cpu_usage, ram_usage, disk_usage) VALUES (?, ?, ?, ?)',
                  ('2023-04-01 12:00:00', 50.0, 60.0, 70.0))
        conn.commit()

        # Вызываем функцию show_history и проверяем, что окно с историей открылось
        show_history()
        self.assertTrue(history_window.winfo_exists())

if __name__ == '__main__':
    unittest.main()