# 6 Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print
year = int(input("Введите год в формате уууу: "))
y = year
if year % 4 != 0:
    y = year, "обычный год"
elif year % 100 == 0:
    if year % 400 == 0:
        y = year, "високосный год"
else:
    y = year, "обычный год"
print(y)

# 7 Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

num = int(input("Введите число от 1 до 999: "))
a = num
i = 1
b = 9
c = 99
d = 999
if i <= a <= b:
    s = a ** 2, "цифра"
elif b < a <= c:
    s = ((a // 10) * (a % 10)), "двузначное число"
elif c < a <= d:
    s = str(a)
    s = s[::-1], "трехзначное число"
else:
    s = num, "число не из диапазона, введите новое число: "
print(s)

# 8 Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
a = int(input("Введите длину отрезка 1: "))
b = int(input("Введите длину отрезка 2: "))
c = int(input("Введите длину отрезка 3: "))
if c >= a + b or b >= a + c or a >= b + c:
    print("Треугольника не существует")
elif a == b and a == c:
    print("Этот треугольник равносторонний")
elif a == b or b == c or c == a:
    print("Этот треугольник равнобедренный")
else:
    print("Этот треугольник разносторонний")

# 9 Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

k = int(input('Введите число: '))

while k < 0 or k > 100000:
    print("Данное число вне диапазона, введите число от 0 до 100 000 ")
    k = int(input('Введите число: '))

i = 1
ost = 1

while i < k and ost != 0:
    i += 1
    ost = k % i
    if ost == 0 and i != k:
        print("Число составное")

if i == k:
    print("Число простое")



# 10 Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайногочисла используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint
num = randint(0, 1000)
print(num)
min_lim = 0
max_lim = 1000
i = 1

while i != 10:
    print('Попытка № ' + str(i))
    i += 1
    text = float(input('Введите число между ' + str(min_lim) + ' и ' + str(max_lim) + ' :'))
    if text > min_lim or text < max_lim:
        if text != num:
            print("Не угадал, загаданное число, попробуй еще")
            if text < num:
                print("Мое число больше")
            else:
                print("Мое число меньше")
        else:
            print('Угадал')
            break
if i == 10:
    print("Попыток больше нет")
    print('Было загадано число' + str(num))




