
# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

# def to_dict(lst):
#     some_dict = {x: x for _ in lst for x in lst}
#     return some_dict

# some_list = [2, 5, 1, 3, 'sd', 'gt']
# print(to_dict(some_list))
# """
#_______________________________________________________________________________

# Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs),
# которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict,
# состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

# my_dict = {'first_one': 'we can do it'}
# def biggest_dict(**kwargs):
#     my_dict.update(**kwargs)
# print(my_dict)
# """
# #_______________________________________________________________________________

# """
# # Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется создать словарь, который в качестве ключей будет принимать данные числа
# # (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию
# # count_it(sequence), принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

# import random
# sequence = ''
# for _ in range(9):
#     sequence += str(random.randint(0, 9)) # Создаём строку со случайными числами
# print(sequence)

# def count_it(sequence):
#     my_dict = {int(x): sequence.count(x) for _ in sequence for x in sequence}  # Заполняем словарь с ключами из строки и значением с количеством повторений ключей
#     sorted_dict = {k: my_dict[k] for k in sorted(my_dict, key=my_dict.get, reverse=True)[:3]}  # Сортируем словарь по количеству повторений на убываение и отрезаем первые 3 значения
#     return sorted_dict

# print(count_it(sequence))
# """
# #_______________________________________________________________________________

# """
# # 4. Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# # а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# # Например: >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# # { "А": { "П": ["Петр Алексеев"] }, "И": { "И": ["Илья Иванов"] }, "С": { "И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"] } }

def thesaurus_adv(*args):
    my_dict = {}
    for elem in args:
        name, last_name = elem.split()
        if not my_dict.get(last_name[0]):
            my_dict[last_name[0]] = { name[0] : [elem] }
        elif not my_dict[last_name[0]].get(name[0]):
            (my_dict[last_name[0]])[name[0]] = [elem]
        else:
            (my_dict[last_name[0]])[name[0]].append(elem)
    return my_dict
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
# """
# #________________________________________________________________________________

