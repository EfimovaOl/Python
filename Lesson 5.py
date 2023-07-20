#Напишите функцию, которая принимает на вход строку-абсолютный путь до файла
#Функция возвращает кортеж из 3 элементов: путь, имя файла, расширение файла

def split_file_path(path):
    dir_path, filename = path.rsplit('/', 1)
    name, file_1 = filename.split('.', 1)
    return dir_path, name, f".{file_1}"

file_path = '/home/user/document/example.txt'
directory, filename, file_extension = split_file_path(file_path)
print("Путь:", directory)
print("Имя файла: ", filename)
print("Расширение файла: ", file_extension)


#Напишите однострочный генератор словаря, который принимает на вход три списка
#одинаковой длины:имена str, ставка int, премия str с указанием процентов вида 10.25%
#В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
#Сумма рассчитывается как ставка умножения на процент премии

def generate_dict(names, stakes, prizes):
    return {name: stake * float(prize.rstrip('%')) / 100
            for name, stake, prize in zip(names, stakes, prizes)}

list_names = ['Elena', 'Sergey', 'Tom']
list_stakes = [1000, 1700, 500]
list_prizes = ['10%', '7.5%', '25.7%']

finish_dict = generate_dict(list_names, list_stakes, list_prizes)
print(finish_dict)

#Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator(n):
    a, k = 0, 1
    for i in range(n):
        yield a
        a, k = k, a + k

num = 10
fibonacci = list(fibonacci_generator(num))

print(fibonacci)