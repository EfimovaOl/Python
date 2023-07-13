# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата

def get_hexadecimal_representation(number):
    hexadecimal = ''

    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)
    while number > 0:
        remainder = str(number % 16)
        hexadecimal = remainder + hexadecimal
        number = number // 16
    if is_negative:
        hexadecimal = '-' + hexadecimal
    return hexadecimal
num = int(input(('Введите целое число: ')))
result = get_hexadecimal_representation(num)
print('Шестнадцатеричное представление числа: ', result)
print('шестнадцатеричное представление числа через hex: ', hex(num))


# Напишите программу, которая принимает две строки вида а/в - дровь с числителем
# и знаменателем. Программа должна возвращать сумму и * произведение дробей.
# Для проверки своего кода используйте модуль fractions
# (1 вариант)
def calculate_fraction_operations(fraction1, fraction2):

    num_1, denom_1 = map(int, fraction1.split('/'))
    num_2, denom_2 = map(int, fraction2.split('/'))

    num_add = num_1 * denom_2 + num_2 * denom_1
    num_mult = num_1 * num_2

    denom_common = denom_1 * denom_2

    gcd_add = greatest_common_divisor(num_add, denom_common)
    gcd_mult = greatest_common_divisor(num_mult, denom_common)

    addition = f"{num_add // gcd_add}/{denom_common // gcd_add}"
    multiplication = f"{num_mult // gcd_mult}/{denom_common // gcd_mult}"

    return addition, multiplication
def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a
f_1 = input('Введите первую дробь в формате a/b: ')
f_2 = input('Введите первую дробь в формате a/b: ')

add, mult = calculate_fraction_operations(f_1, f_2)
print('Сумма дробей: ', add)
print("Произведение дробей: ", mult)

from fractions import Fraction
f1 = Fraction(f_1)
f2 = Fraction(f_2)
print('Проверка с использованием модуля fractions: ')
print('Сумма дробей (fractions): ', f1 + f2)
print('Произведение дробей ( fractions): ', f1 * f2)

#2 (вариант)
import fractions

first: str = input("Введите числитель первой дроби: ")
second: str = input("Введите знаменатель первой дроби:  ")
third: str = input("Введите числитель второй дроби: ")
fourth: str = input("Введите знаменатель второй дроби: ")
number1: int = int(first)
number2: int = int(second)
number3: int = int(third)
number4: int = int(fourth)

result1 = (number1 / number2) + (number3 / number4)
result2 = (number1 / number2) * (number3 / number4)
print(result1)
print(result2)
first_fraction = fractions.Fraction(number1, number2)
second_fraction = fractions.Fraction(number3, number4)
result3 = first_fraction + second_fraction
result4 = first_fraction * second_fraction
print(result3)
print(result4)
