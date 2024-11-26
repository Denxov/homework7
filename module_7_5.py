import os, time

directory = "."
os.chdir(r'd:\.')
for root, dirs, files in os.walk(directory):
    for file in files:
        if os.path.exists(file):
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(file)
            filesize = os.path.getsize(file)
            parent_dir = os.path.pardir
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
                f' Родительская директория: {parent_dir}')
