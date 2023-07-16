# Напишите функцию для транспонирования матрицы

def transpose(table):
    table2 = []

    for i in range(len(table[0])):
        table2.append(list())
        for j in range(len(table)):
            table2[i].append(table[j][i])
        return table2

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
matrix2 = transpose(matrix)
print(matrix2)


# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def dictionary(one, two):
     dict = {
         f'{one}': id(one),
         f'{two}': id(two)
     }
     return dict
a = 1
b = 2
dic = dictionary(a, b)
print(dic)




