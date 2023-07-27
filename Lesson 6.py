#Создайте модуль и напишите в нем функцию, которая
#получает на вход дату в формате DD.MM.YYYY
#Функция возвращает истину, если дата может существовать или ложь,
#если такая дата невозможна
#Для простоты договоримся, что год может быть в диапазоне[1,9999]
#Весь период [1 января 1 год - 31 декабря 9999 года]
#действует Григорианский календарь. Проверку года на високосность вынестив отдельную
#защищенную функцию.

from sys import argv

def _is_leap(year: int) -> bool:
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)

def valid(full_date: str) -> bool:
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and _is_leap(year) and date > 29:
        return False
    if month == 2 and not _is_leap(year) and date > 28:
        return False
    return True

if __name__ == '__main__':
    print(valid("30.2.2001"))

    if len(argv) != 2:
        print('Использование: python date_validator.py <дата в формате DD.MM.YYYY>')
    else:
        input_date = argv[1]
        if valid(input_date):
            print('Дата существует.')
        else:
            print('Дата не существует')

#Создайте пакет со всеми модулями, которые вы создали за время занятий
#Добавьте в __init__ пакета имена модулей внутри дандер __all__
#В модулях создайте дандер __all__ и укажите только те функции, которые
#могут работать за пределами модуля

__all__ = ['number', 'text', 'date']
__all__ = ['guess']
__all__ = ['secrets', 'storage']
__all__ = ['valid']

# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import itertools
import random

def are_queens_attacking_each_other(queens_positions):

    """
    функция для проверки
    Args:
        queens_positions(list):
    Returns:
            bool: True, если ферзи не атакуют друг друга, иначе False
    """
    for i in range(len(queens_positions)):
        for j in range(i + 1, len(queens_positions)):
            row1, col1 = queens_positions[i]
            row2, col2 = queens_positions[j]

            if row1 == row2 or col1 == col2 or abs(row1 + row2) == abs(col1 + col2):
                return False
    return True

def generate_successful_arrangements():
    """
    Returns:
        list:
    """
    successful_args = []

    all_permutations = list(itertools.permutations(range(1, 9)))

    random.shuffle(all_permutations)

    for permutation in all_permutations:
        queens_positions = [(i + 1, permutation[i]) for i in range(8)]

        if are_queens_attacking_each_other(queens_positions):
            successful_args.append(queens_positions)
            if len(successful_args) == 4:
                break
    return successful_args

successful_arrangements = generate_successful_arrangements()

print(f'успешная расстановка ферзей: ')

for i, arrangement in enumerate(successful_arrangements, 1):
    print(f'расстановка {i}: {arrangement}')
