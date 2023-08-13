# 1.Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Fish(Animal):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth
    def get_info(self):
        return f'Глубина обитания {self.name} = {self.depth} m'

class Reptiles(Animal):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def get_info(self):
        return f'Длина тела {self.name} = {self.length} m'

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def get_info(self):
        return f'Порода собаки {self.name} = {self.breed}'


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def get_info(self):
        return f'Порода кошки {self.name} = {self.breed}'


class AnimalFactory:
    def __init__(self):
        self.animal_classes = {
            'Fish': Fish,
            'Reptiles': Reptiles,
            'Dog': Dog,
            'Cat': Cat
        }

    def create_animal(self, animal_type, *args):
        if animal_type not in self.animal_classes:
            raise ValueError('Invalid animal type')

        animal_class = self.animal_classes[animal_type]
        return animal_class(*args)


if __name__ == "__main__":
    factory = AnimalFactory()

    fish = factory.create_animal('Fish', 'Dorado', 0.7)
    reptile = factory.create_animal('Reptiles', 'Snake', 2.0)
    dog = factory.create_animal('Dog', 'Adele', 'Jack russel')
    cat = factory.create_animal('Cat', 'Masya', 'Siamese')

    print(fish.get_info())
    print(reptile.get_info())
    print(dog.get_info())
    print(cat.get_info())



# 2.Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных),
# которые вы уже решали.
# Превратите функции в методы класса,
# а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

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
from random import randint

class CSVManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def generate_numbers_to_csv(self):
        with open(self.file_name, 'w', newline='', encoding='utf-8') as f_write:
            csv_write = csv.writer(f_write, dialect='excel')
            csv_write.writerow(["a", "b", "c"])
            csv_write.writerows([[randint(-100, 100), randint(-100, 100)]
                                 for _ in range(randint(100, 1000))])


class JSONManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def save_to_json(self, data):
        with open(self.file_name, "w", encoding="utf-8") as f_write:
            json.dump(data, f_write, indent=2, ensure_ascii=False)

    def load_from_json(self):
        data = {}
        if os.path.exists(self.file_name):
            with open(self.file_name, "r", encoding="utf-8") as f_read:
                data = json.load(f_read)
        return data

class QuadraticEquationSolver:
    def __init__(self, a=1, b=1, c=1):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if self.a == 0:
            return 'Коэффициент (a) = 0'
        d = self.b ** 2 - 4 * self.a * self.c
        x_1 = (-self.b + d ** 0.5) / (2 * self.a)
        x_2 = (-self.b - d ** 0.5) / (2 * self.a)
        if d > 0:
            result = f'2 корня: {x_1} и {x_2}'
        elif d == 0:
            result = f'1 корень: {x_1}'
        else:
            result = f'комплексные корни: {x_1} и {x_2}'

        return result

if __name__ == "__main__":
    file_name = 'data.csv'
    csv_manager = CSVManager(file_name)
    csv_manager.generate_numbers_to_csv()

    with open(file_name, newline='') as f_read:
        f_read.readline()
        for line in f_read:
            a, b, c = map(int, line.split(","))
            solver - QuadraticEquationSolver(a, b, c)
            result = solver.solve()

            json_file_name = f"{solver.a}_{solver.b}_{solver.c}.json"
            json_manager = JSONManager(json_file_name)
            data = json_manager.load_from_json()
            data[str((solver.a, solver.b, solver.c))] = result
            json_manager.save_to_json(data)
