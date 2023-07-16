 # Дан список повторяющихся элементов.
 # Вернуть список с дублирующимися элементами.
 # В результирующем списке не должно быть дубликатов.

def find_duplication(my_lst):
    return list(set([x for x in my_lst if my_lst.count(x) > 1]))

my_lst = [1, 3, 5, 5, 35, 17 ,17 ,1, 35, 18]
print(find_duplication(my_lst))


# В большой текстовой строке подсчитать количество встречаемых слов
# и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text = "Сангрию можно приготовить из самых разнообразных ингредиентов." \
     "Вкусовые качества напитка могут значительно варьироваться в зависимости от вида фруктов и ликёра," \
     "использованных при приготовлении. Некоторые также добавляют газированную воду," \
     "придавая напитку игристость. Другие вообще готовят сангрию на основе белого вина." \
     "Летом рекомендуется подавать напиток хорошо охлаждённым, зимой — подогретым, сдобренным корицей," \
     "гвоздикой и мускатным орехом."


text_list = text.lower().split()
text_dict = {}
for i in text_list:
    a = i.strip(".,!:;")
    if a not in text_dict:
        text_dict[a] = 1
    else:
        text_dict[a] += 1
print(text_dict)

# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав
# его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

items = {'tent': 5, 'water': 3, 'food': 4, 'clothes': 2, 'first aid kit': 1}
max_weight = 10
print(pack_backpack(items, max_weight))