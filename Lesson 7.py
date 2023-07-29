# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from string import ascii_lowercase, digits
from random import randint, choices

def create_files(extension: str, min_len_name: int = 6, max_len_name: int = 30,
                 min_size_file: int = 256, max_size_file: int = 4096, amount_file: int = 42) -> None:
    for _ in range(amount_file):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len_name, max_len_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size_file, max_size_file)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    create_files('bin', amount_file=1)


#  Доработаем предыдущую задачу
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.


def gen_files(**kwargs) -> None:
    for extension, amount_file in kwargs.items():
        create_files(extension=extension, amount_file=amount_file)


if __name__ == '__main__':
    gen_files(bin=2, jpg=1)

# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from pathlib import Path
from random import choices, randint
from string import ascii_lowercase, digits


def create_files(extension: str, min_len_name: int = 6, max_len_name: int = 30,
                 min_size_file: int = 256, max_size_file: int = 4096, amount_file: int = 42) -> None:
    for _ in range(amount_file):
        print(Path.cwd())
        while True:
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len_name, max_len_name)))
            if not Path(f'{name}.{extension}').is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size_file, max_size_file)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)

def gen_files(path: str | Path, **kwargs) -> None:
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
        os.chdir(path)
    for extension, amount_file in kwargs.items():
        create_files(extension=extension, amount_file=amount_file, min_len_name=1, max_len_name=1)


if __name__ == '__main__':
    gen_files('C:/Users/Sonya/PycharmProjects/pythonProject', bin=2, jpg=10)

# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки

from os import chdir
from pathlib import Path

def sort_files(path: Path, groups: dict[Path, list[str]] = None) -> None:
    chdir(path)

    if groups is None:
        groups = {
            Path('video'): ['avi', 'mkv'],
            Path('image'): ['ipg', 'png'],
            Path('text'): ['txt', 'doc'],
        }
    reversed_groups = {}
    for target_dir, extension_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        for extension in extension_list:
            reversed_groups[f'.{extension}'] = target_dir

    for file in path.iterdir():
        if file.is_file() and file.suffix in reversed_groups.keys():
            file.replace(reversed_groups[file.suffix] / file.name)

if __name__ == '__main__':
    sort_files(Path('C:/Users/Sonya/PycharmProjects/pythonProject'))


# 2.Напишите функцию группового переименования файлов. Она должна:
# * -- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# * -- принимать параметр количество цифр в порядковом номере.
# * -- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# * -- принимать параметр расширение конечного файла.
# * -- принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

def group_ren(desired_name, num_digits, source_ext, target_ext, name_range=None):
    files = [f.split(source_ext)[0] for f in os.listdir('.')
             if os.path.isfile(f) and f.endswith(source_ext)]

    if not files:
            print('Файлы с заданным расширением не найдены')
            return
    for i, file in enumerate(files, 1):
        if name_range:
            start, end = name_range
            base_name = file[start - 1:end]
        new_name = base_name + desired_name + f"{i:0{num_digits}}" + target_ext
        os.rename(f'{file}{source_ext}', new_name)
        print(f"Переименован файл {file} в {new_name}")
group_ren("_new", 6, "txt", ".doc", name_range=[3,6])



# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
