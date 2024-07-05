# Программа переименовывает файлы в указанной папке добавляя к имени файла дату изменения файла
import os, time
from datetime import datetime


DIRECTORY = r"C:\PycharmProjects\pythonProject\Переименование файлов по ообразцу\files"
DATE_FORMAT = '%d.%m.%Y' #'%d.%m.%Y %H:%M:%S'


def rename_files(find_directory): # Функция выводит список файлов в указанной директории
    for root, dirs, files in os.walk(find_directory):
        for name in files:
            rename_file(root, name)


def rename_file(root, name):
    valid_name = get_valid_name(name)
    old_file = os.path.join(root, name)
    new_file = os.path.join(root, valid_name)
    os.rename(old_file, new_file)


def get_valid_name(name):
    name = name[:-4] + '_' + datetime.fromtimestamp(os.stat(DIRECTORY).st_atime).strftime(DATE_FORMAT) + name[-4:]
    return name


if __name__ == '__main__':
    rename_files(DIRECTORY)
