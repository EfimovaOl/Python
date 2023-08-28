# Решить задания, которые не успели решить на семинаре.
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class ValidateSize:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name.capitalize()} cannot be negative.")
        instance.__dict__[self.name] = value

class Rectangle:
    width = ValidateSize('_width')
    height = ValidateSize('_height')

    def __init__(self,width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimetr(self):
        return 2 * (self._width + self._height)

rectangle = Rectangle(4, 5)
print("Width:", rectangle.width)
print("Height:", rectangle.height)
print("Area:", rectangle.area)
print("Perimetr:", rectangle.perimetr)

rectangle.width = 6
rectangle.height = 8
print("Update Width:", rectangle.width)
print("Update Height:", rectangle.height)
print("Update Area:", rectangle.area)
print("Update Perimetr:", rectangle.perimetr)

try:
    rectangle.width = -2
except ValueError as e:
    print("Error:", e)

try:
    rectangle.height = -3
except ValueError as e:
    print("Error:", e)


# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета
# и по оценкам всех предметов вместе взятых.

import csv
import os

class NameValidator:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not all(i.isalpha() for i in value.split()):
            raise ValueError("Name should contain only letters.")
        if not all(i.istitle() for i in value.split()):
            raise ValueError("Name should start with an uppercase letter. ")
        instance._name = value

class Student:
    name = NameValidator()

    def __init__(self, name, subjects_file):
        self.name = name
        if os.path.exists(subjects_file):
            self.subjects = self.load_sub(subjects_file)
            self.scores = {subject: {"grades": [], "test_results": []} for subject in self.subjects}
        else:
            self.subjects = []
            self.scores = {}

    def load_sub(self, subjects_file):
        with open(subjects_file, 'r') as file:
            reader = csv.reader(file)
            subjects = next(reader)
        return subjects

    def __call__(self, subject, grade, test_result):
        if subject not in self.subjects:
            raise ValueError(f"{subject} is not a valid subject.")
        if grade < 2 or grade > 5:
            raise ValueError("Grade should be between 2 and 5.")
        if test_result < 0 or test_result > 100:
            raise ValueError("Test result should be between 0 and 100.")
        self.scores[subject]["grades"].append(grade)
        self.scores[subject]["test_results"].append(test_result)

    def calc_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"{subject} is not a valid subject.")
        test_results = self.scores[subject]["test_results"]
        if not test_results:
            return 0
        return sum(test_results) / len(test_results)


    def calc_average_grade(self):
        total_grades = []
        total_subjects = 0
        for subject in self.subjects:
            total_grades.extend(self.scores[subject]["grades"])
            total_subjects += len(self.scores[subject]["grades"])
        if not total_grades:
            return 0
        return sum(total_grades) / total_subjects

student = Student("Difanova Svetlana Petrovna", "subjects.csv")

student("Math", 5, 99)
student("History", 4, 80)
student("English language", 5, 90)
student("Physical Culture", 3, 70)
student("Biology", 4, 85)

print("Name:", student.name)
print("Subjects:", student.subjects)
print("Math average test score:", student.calc_average_test_score("Math"))
print("Overall average grade:", student.calc_average_grade())
print(student.scores)