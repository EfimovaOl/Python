# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

from typing import Callable, TextIO


def repeat_runs(count: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrap(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

            return wrap

        return decorator


repeat_runs(count=33)
def print_hello():
    print("Privet!!!")


print_hello()

# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.

import json
import os
from functools import wraps
from random import randint
from typing import Callable

def param(func: Callable) -> Callable[[int, int], None]:
    @wraps(func)
    def wrapper(*args):
        if not args[0] in range(1, 101) or not args[1] in range(1, 11):
            return func(randint(1, 100), randint(1, 10))
        return func(*args)

    return wrapper

def repeate_run(count: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return wrapper

    return decorator

def fun_log(func: Callable) -> Callable[..., None]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        res_dict = {}
        name = f"{func.__name__}.json"
        if os.path.exists(name):
            with open(name, encoding="utf-8") as json_f:
                res_dict = json.load(json_f)

        with open(name, "w", encoding="utf-8") as json_f:
            res_dict[str(args)] = args
            res_dict.update(**kwargs)
            res_dict["result"] = func(*args, **kwargs)
            json.dump(res_dict, json_f, indent=2, ensure_ascii=False)

    return wrapper

@fun_log
@param
@repeate_run(count=2)

def guess_num(num: int, count: int):
    secret = randint(1, num)
    print(f"Отгадай число от 1 до {num}. {count} попыток.")

    for attempt in range(count):
        guess = int(input(f"Попытка № {attempt + 1}: "))

        if guess < secret:
            print("Число больше.")
        elif guess > secret:
            print("Число меньше.")
        else:
            print("Супер! Угадали.")
            break


if __name__ == "__main__":
    #guess_num(20,5)
    print(help(guess_num))

#  Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.


import csv
import json
import os.path
from functools import wraps
from random import randint

def calc(func):
    @wraps(func)
    def wrapper():
        file_name = f"{func.__name__}.csv"
        gen_num_to_csv(file_name)
        with open(file_name, newline='')as f_read:
            f_read.readline()
            for line in f_read:
                func(*map(int, line.split(",")))

    return wrapper

def save_to_json_dec(func):
    @wraps(func)
    def wrapper(*args):
        all_data = {}
        file_name = f"{func.__name__}.json"
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as f_read:
                all_data = json.load(f_read)
        with open(file_name, "w", encoding="utf-8") as f_write:
            all_data[str(args)] = func(*args)
            json.dump(all_data, f_write, indent=2, ensure_ascii=False)

    return wrapper

def gen_num_to_csv(file_name):
    with open(file_name, 'w', newline='', encoding="utf-8") as f_write:
        csv_write = csv.writer(f_write,dialect='excel')
        csv_write.writerow(['a', 'b', 'c'])
        csv_write.writerows([[randint(-100, 100), randint(-100, 100), randint(-100, 100)]]
                            for _ in range(randint(100, 1000)))

@save_to_json_dec

def find_roots(a=1, b=1, c=1):
    if a == 0:
        return 'коэффициент (a) = 0'
    d = b ** 2 - 4 * a * c
    x_1 = (-b + d ** 0.5) / (2 * a)
    x_2 = (-b - d ** 0.5) / (2 * a)
    if d > 0:
        result = f'2 корня: {x_1 = } и {x_2 = }'
    elif d == 0:
        result = f'1 корень: {x_1 = }'
    else:
        result = f' комплексные корни: {x_1 = } и {x_2 = }'
    return result


if __name__ != "__main__":
    find_roots()