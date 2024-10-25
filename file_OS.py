import os
import time

directory = "." # Текущая директория

#обход каталога
for root, dirs, files in os.walk(directory):
    for file in files:
        #путь к файлу
        filepath = os.path.join(root, file)

        #время изменения файла
        filetime = os.path.getmtime(filepath)

        #Форматируем время изменения
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        #размер файла
        filesize = os.path.getsize(filepath)

        #оснавная директория файла
        parent_dir = os.path.dirname(filepath)

        #информацию о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
