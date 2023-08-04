# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноименных pickle файлов

import json
import os
import pickle
from pathlib import Path


def json_pickle(file_new_folder):
    for i in os.listdir(file_new_folder):
        if i.endswith(".json"):
            with (open(i.replace(".json", ".pickle"), "wb") as f_pickle,
                  open(i) as f_json):
                pickle.dump(f_json.read(), f_pickle)


if __name__ == "__main__":
    json_pickle(Path.cwd())

# Напишите функцию, которая преобразунт pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестирования возьмите pickle версию файла из задачи 5 .
# Функция должна извлекать ключи для заголовков
# столбца из переданного файла.

import csv
import pickle
from pathlib import Path


def conv_to_csv(file_name: Path) -> None:
    with(open(file_name, 'rb') as f_pickle,
         open(f'{file_name.stem}.csv', "w", newline='', encoding='utf-8') as f_csv):
        new_dict = pickle.load(f_pickle)

        csv_write = csv.writer(f_csv, dialect='excel', delimiter=',')
        csv_write.writerow(new_dict.keys())

        n = [str(i).split() for i in new_dict.values()]
        csv_write.writerows(n)


if __name__ != "__main__":
    conv_to_csv(Path("names.pickle"))

# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictWriter
# Распечатайте его как pickle строку

import csv
import pickle
from pathlib import Path


def print_pickl_str(file_name: Path) -> None:
    with open(file_name, "r", newline='', encoding='utf-8') as f_csv:
        print(pickle.dumps(f_csv.read()))


if __name__ != "__main__":
    print_pickl_str(Path("new_user.csv"))

# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит ее и все вложенные директории. Результаты обхода сохраните в файлы
# json, csv, pickle
# Для дочерних объектов указывайте родительскую директорию
# Для каждого объекта укажите файл это или директория
# Для файлов сохраните его в байтахб а для директории размер
# файлов в ней с учетом всех вложенных файлов и директорий


import json
import os
import csv
from pathlib import Path
import pickle

def get_sz(directory):
    total_sz = 0
    for dir_path, dir_name, file_name in os.walk(directory):
        for filename in dir_name:
            filepath = os.path.join(dir_path, filename)
            total_sz += os.path.getsize(filepath)
    return total_sz

def collection(files_path):
    data = []
    for dir_path, dir_name, file_name in os.walk(files_path):
        for name in dir_name:
            little_path = os.path.join(dir_path, name)
            size = get_sz(little_path)
            data.append({
                'name': name,
                'type': 'directory',
                'parent_directory': dir_path,
                'size': size
            })
        for name in file_name:
            filepath = os.path.join(dir_path, name)
            size = os.path.getsize(filepath)
            data.append({
                'name': name,
                'type': 'file',
                'parent_directory': dir_path,
                'size': size
            })

    with (open('directory_data.json', 'w') as json_file,
          open('directory_data.csv', 'w', newline='') as csv_file,
          open('directory_data.pickle', 'wb') as pickle_file):

        json.dump(data, json_file, indent=2)

        fieldnames = ['name', 'type', 'parent_directory', 'size']
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

        pickle.dump(data, pickle_file)

if __name__ == '__main__':
    collection(Path.cwd())